# Zero-Downtime Deployment Checklist

A practical zero-downtime deployment checklist for DevOps, SRE, platform and backend teams that need safer production releases.

Created by **SteadyOps**:
https://steadyops.best/

Related SteadyOps article:
https://steadyops.best/articles/zero-downtime-bluegreen-deployments/

## Why this exists

Zero-downtime deployment is not only about replacing containers or restarting services carefully.

A safe production deployment needs:

* health checks
* rollback path
* database migration strategy
* load balancer behavior
* observability
* deployment gates
* customer-impact validation
* clear ownership

This checklist helps teams prepare deployment workflows that reduce outage risk and make rollback decisions easier.

## When to use this checklist

Use it before deploying:

* web applications
* backend APIs
* Kubernetes services
* Docker-based services
* nginx / HAProxy-routed applications
* PostgreSQL-backed applications
* services with background workers
* customer-facing SaaS features
* high-risk infrastructure changes

## Deployment strategies

| Strategy                  | Best for                  | Risk        | Notes                                        |
| ------------------------- | ------------------------- | ----------- | -------------------------------------------- |
| Rolling deployment        | Small stateless services  | Medium      | Requires good readiness checks               |
| Blue/Green deployment     | Critical web/API services | Low/Medium  | Needs traffic switch and rollback plan       |
| Canary release            | High-risk changes         | Low/Medium  | Needs strong metrics and progressive traffic |
| Feature flags             | Product behavior changes  | Low         | Requires flag ownership and cleanup          |
| Manual maintenance window | Legacy systems            | Medium/High | Not zero-downtime, but sometimes realistic   |

## Pre-deployment checklist

Copy this section into your release ticket or runbook.

````md
# Zero-Downtime Deployment Checklist

## 1. Release summary

Service:

Version:

Deployment owner:

Rollback owner:

Planned deployment time:

Expected customer impact:

Deployment strategy:

- [ ] Rolling
- [ ] Blue/Green
- [ ] Canary
- [ ] Feature flag
- [ ] Other:

## 2. Readiness checks

- [ ] Health endpoint exists
- [ ] Readiness probe is configured
- [ ] Liveness probe is configured
- [ ] Startup probe is configured if service starts slowly
- [ ] Health check validates real dependencies where appropriate
- [ ] Service does not receive traffic until ready
- [ ] Graceful shutdown is configured
- [ ] Existing connections are drained before termination
- [ ] Background workers shut down safely
- [ ] Deployment timeout is defined

## 3. Observability checks

- [ ] Error rate dashboard is ready
- [ ] p95/p99 latency dashboard is ready
- [ ] Request rate is visible
- [ ] Saturation metrics are visible
- [ ] Database connections are visible
- [ ] Queue depth is visible
- [ ] Logs are searchable
- [ ] Alerts are enabled
- [ ] Deployment event is annotated in monitoring

## 4. Rollback checks

- [ ] Previous version is known
- [ ] Previous artifact/image is available
- [ ] Rollback command is documented
- [ ] Rollback was tested in staging
- [ ] Rollback owner is online
- [ ] Rollback validation steps are defined
- [ ] Rollback decision threshold is defined

## 5. Database migration checks

- [ ] Migration is backward-compatible
- [ ] Migration does not break the previous application version
- [ ] Destructive changes are split into a later release
- [ ] Long-running migration was tested on realistic data volume
- [ ] Locking risk was reviewed
- [ ] Backup exists before migration
- [ ] Restore/fallback plan exists
- [ ] Application can run during migration

## 6. Load balancer / ingress checks

- [ ] nginx / HAProxy / ingress routes are valid
- [ ] Upstream health checks are configured
- [ ] Connection draining is enabled where possible
- [ ] Timeouts are reviewed
- [ ] TLS certificate is valid
- [ ] DNS changes are not part of the release unless planned
- [ ] Old and new versions can coexist during traffic switch

## 7. Deployment commands

Application deployment:

```bash
# Example:
# kubectl rollout status deployment/my-service
````

Rollback:

```bash
# Example:
# kubectl rollout undo deployment/my-service
```

Helm rollback:

```bash
# Example:
# helm history my-release
# helm rollback my-release 12
```

Argo Rollouts:

```bash
# Example:
# kubectl argo rollouts get rollout my-service
# kubectl argo rollouts abort my-service
# kubectl argo rollouts promote my-service
```

## 8. Deployment validation

* [ ] Service returns HTTP 200
* [ ] Main customer flow works
* [ ] Error rate is normal
* [ ] p99 latency is normal
* [ ] Database connections are stable
* [ ] Queue depth is not growing unexpectedly
* [ ] No restart loop
* [ ] No unusual logs
* [ ] Business-critical endpoint is tested
* [ ] Monitoring remains normal for at least 10-15 minutes

## 9. Rollback decision criteria

Rollback if one or more conditions are true:

* [ ] 5xx error rate exceeds agreed threshold
* [ ] p99 latency is more than 2x baseline
* [ ] queue depth grows and does not recover
* [ ] database connection saturation appears
* [ ] customer-facing flow is broken
* [ ] security or authentication flow is broken
* [ ] data corruption is suspected
* [ ] deployment cannot finish within the agreed window

## 10. Communication

Internal deployment channel:

Deployment started at:

Deployment completed at:

Rollback decision deadline:

Customer communication needed: yes/no

Post-deployment summary:

````

## Kubernetes examples

Check rollout status:

```bash
kubectl rollout status deployment/my-service
````

Rollback to previous revision:

```bash
kubectl rollout undo deployment/my-service
```

Rollback to specific revision:

```bash
kubectl rollout undo deployment/my-service --to-revision=3
```

View rollout history:

```bash
kubectl rollout history deployment/my-service
```

Pause rollout:

```bash
kubectl rollout pause deployment/my-service
```

Resume rollout:

```bash
kubectl rollout resume deployment/my-service
```

## Helm examples

View release history:

```bash
helm history my-release
```

Rollback to revision:

```bash
helm rollback my-release 12
```

Watch pods after rollback:

```bash
kubectl get pods -w
```

## Argo Rollouts examples

Check rollout:

```bash
kubectl argo rollouts get rollout my-service
```

Abort rollout:

```bash
kubectl argo rollouts abort my-service
```

Promote rollout:

```bash
kubectl argo rollouts promote my-service
```

## Database migration rules

For zero-downtime deployments, avoid migrations that require old and new application versions to switch at the same exact moment.

Safer approach:

1. Add new nullable column or table.
2. Deploy application version that writes both old and new formats.
3. Backfill data.
4. Deploy application version that reads the new format.
5. Remove old column/table in a later release.

Avoid:

* dropping columns used by the old version
* renaming columns without compatibility layer
* long locks during peak traffic
* irreversible migrations without backup
* application code that requires migration to finish instantly

## Common zero-downtime deployment mistakes

* Health check returns 200 before the service is actually ready
* Readiness probe does not check critical dependencies
* Old and new versions cannot run at the same time
* Database migration breaks rollback
* Background workers process incompatible messages
* Load balancer sends traffic to terminating pods
* Rollback command exists but was never tested
* Metrics are checked after customers already complain
* Deployment owner and rollback owner are the same overloaded person
* Feature flags are created but never cleaned up

## Post-deployment review

After the deployment, record:

* what changed
* what went well
* what almost failed
* whether rollback would have worked
* whether metrics were enough
* whether alerts fired correctly
* what should be automated before the next release

## Related SteadyOps resources

* DevOps/SRE articles: https://steadyops.best/articles/
* Zero-Downtime Blue/Green Deployments: https://steadyops.best/articles/zero-downtime-bluegreen-deployments/
* Kubernetes Rollback Checklist: https://steadyops.best/articles/kubernetes-rollback-checklist-for-production-deployments/
* SteadyOps Platform Story: https://steadyops.best/steadyops-platform-case-study/

## About SteadyOps

SteadyOps provides senior DevOps/SRE support for teams that need reliable production systems, safer deployments, monitoring, incident response and recovery runbooks.

Website: https://steadyops.best/

## License

MIT License. Use, adapt and improve this checklist for your own deployment workflow.
