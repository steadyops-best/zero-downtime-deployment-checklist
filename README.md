# Zero-Downtime Deployment Checklist

A practical checklist for DevOps, SRE, platform and backend teams that need safer production releases without relying on memory during deployment windows.

Use it before rolling, blue/green, canary or feature-flagged deployments for web applications, APIs, Kubernetes services, Docker workloads, Nginx/HAProxy routed apps, PostgreSQL-backed services and background workers.

## What this checklist protects against

- Traffic reaching an instance before it is ready.
- Rollback commands that exist but were never tested.
- Database migrations that make rollback unsafe.
- Load balancer or ingress behavior that keeps sending traffic to terminating instances.
- Monitoring gaps where customers notice the problem before the team does.
- Background workers processing incompatible messages after a release.

## Quick release readiness check

Copy this into a release ticket before a production deployment.

```md
## Zero-downtime deployment readiness

Service:
Version:
Deployment owner:
Rollback owner:
Deployment strategy:
Expected customer impact:

### Readiness
- [ ] Health endpoint exists and reflects real readiness.
- [ ] Readiness probe prevents traffic before the app is ready.
- [ ] Graceful shutdown and connection draining are configured.
- [ ] Background workers can stop safely.
- [ ] Deployment timeout is defined.

### Observability
- [ ] Error rate dashboard is ready.
- [ ] p95/p99 latency is visible.
- [ ] Request rate and saturation metrics are visible.
- [ ] Database connections are visible.
- [ ] Queue depth is visible.
- [ ] Logs are searchable.
- [ ] Deployment event is annotated in monitoring.

### Rollback
- [ ] Previous version is known.
- [ ] Previous image/artifact is available.
- [ ] Rollback command is documented.
- [ ] Rollback was tested outside production.
- [ ] Rollback validation steps are defined.
- [ ] Rollback decision threshold is agreed.

### Database changes
- [ ] Migration is backward-compatible.
- [ ] Old and new app versions can run at the same time.
- [ ] Destructive changes are split into a later release.
- [ ] Locking risk was reviewed.
- [ ] Backup exists before migration.
- [ ] Restore or fallback path is known.

### Traffic and routing
- [ ] Nginx, HAProxy or ingress routes are valid.
- [ ] Upstream health checks are configured.
- [ ] Connection draining is enabled where possible.
- [ ] TLS certificate is valid.
- [ ] DNS changes are not bundled into the release unless planned.
```

## Deployment strategy notes

| Strategy | Good fit | Main risk |
| --- | --- | --- |
| Rolling deployment | Small stateless services | Bad readiness checks can leak traffic to broken pods. |
| Blue/green deployment | Critical web/API services | Traffic switch and rollback path must be tested. |
| Canary release | High-risk changes | Requires metrics that show customer impact quickly. |
| Feature flags | Product behavior changes | Flags need ownership and cleanup. |
| Maintenance window | Legacy or stateful systems | Not zero-downtime, but sometimes the honest option. |

## Useful commands

Kubernetes rollout:

```bash
kubectl rollout status deployment/my-service
kubectl rollout history deployment/my-service
kubectl rollout undo deployment/my-service
kubectl rollout undo deployment/my-service --to-revision=3
```

Helm rollback:

```bash
helm history my-release
helm rollback my-release 12
kubectl get pods -w
```

Argo Rollouts:

```bash
kubectl argo rollouts get rollout my-service
kubectl argo rollouts abort my-service
kubectl argo rollouts promote my-service
```

## Safer database migration pattern

Avoid migrations that require old and new application versions to switch at the same exact moment.

1. Add a new nullable column or table.
2. Deploy code that can write both old and new formats.
3. Backfill data.
4. Deploy code that reads the new format.
5. Remove old structures in a later release.

Avoid dropping columns used by the previous version, long locks during peak traffic, irreversible migrations without backup, and app code that assumes migration completion is instant.

## Rollback decision criteria

Rollback if one or more of these conditions are true:

- 5xx error rate exceeds the agreed threshold.
- p99 latency is more than 2x the normal baseline.
- Queue depth grows and does not recover.
- Database connection saturation appears.
- A customer-facing flow is broken.
- Authentication or authorization is broken.
- Data corruption is suspected.
- Deployment cannot finish within the agreed window.

## Post-deployment review

After the release, record:

- what changed
- what went well
- what almost failed
- whether rollback would have worked
- whether metrics were enough
- whether alerts fired correctly
- what should be automated before the next release

## SteadyOps resources

- Website: https://steadyops.best/
- DevOps/SRE articles: https://steadyops.best/articles/
- LinkedIn: https://www.linkedin.com/in/yuri-osipov-0876b0254
- Related article: https://steadyops.best/articles/zero-downtime-bluegreen-deployments/
- Kubernetes rollback article: https://steadyops.best/articles/kubernetes-rollback-checklist-for-production-deployments/
- SteadyOps platform case study: https://steadyops.best/steadyops-platform-case-study/

## Related public checklists

- Kubernetes rollback checklist: https://github.com/steadyops-best/kubernetes-rollback-checklist
- Disaster recovery runbook template: https://github.com/steadyops-best/disaster-recovery-runbook-template

## License

MIT License. Use, adapt and improve this checklist for your own deployment workflow.
