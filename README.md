# Zero-Downtime Deployment Checklist

A reusable release-safety package for rolling, Blue/Green, canary, and feature-flagged deployments. It helps teams define readiness, traffic-switch criteria, rollback safety, database compatibility, observability, and post-release evidence before customer traffic is at risk.

- Canonical implementation guide: https://steadyops.best/articles/zero-downtime-bluegreen-deployments/
- Kubernetes rollback guide: https://steadyops.best/articles/kubernetes-rollback-checklist-for-production-deployments/
- SteadyOps resource library: https://steadyops.best/resources/
- License: MIT
- Artifact version: 1.0.0
- Repository reviewed: 2026-07-12

## Why this repository exists

“Zero downtime” is not a deployment command or a platform feature. It is an operating result that depends on:

- real readiness checks;
- graceful shutdown and connection draining;
- enough healthy capacity during the change;
- observable customer impact and saturation;
- backward-compatible data and message changes;
- a known rollback target and decision owner;
- a controlled traffic switch;
- technical validation plus a critical business transaction;
- retained release evidence.

This repository keeps the compact, forkable artifact separate from the longer explanatory guide so teams can adapt it to their own deployment system without duplicating the canonical article.

## Start here

1. Open [`checklist.md`](checklist.md).
2. Copy it into a release ticket, service repository, runbook, or change-management system.
3. Replace service names, environments, owners, thresholds, strategy, commands, and business-flow checks.
4. Confirm old and new versions can coexist during the deployment and rollback window.
5. Test readiness, shutdown, traffic removal, rollback, and smoke validation in stage or another production-like environment.
6. Complete [`release-evidence-template.md`](release-evidence-template.md) during or immediately after the release.
7. Store the completed checklist and evidence record with deployment logs, dashboards, approvals, and follow-up work.

## Repository contents

| File | Purpose |
|---|---|
| [`checklist.md`](checklist.md) | Compact release contract covering readiness, observability, rollback, traffic switch, and post-deployment checks. |
| [`release-evidence-template.md`](release-evidence-template.md) | Release identity, compatibility, traffic timeline, production signals, rollback readiness, and final outcome record. |
| [`CITATION.cff`](CITATION.cff) | Citation metadata for internal release standards and derived runbooks. |
| [`LICENSE`](LICENSE) | MIT license for reuse and adaptation. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Rules for safe, practical improvements. |

## Release-safety model

### 1. Define the release contract

Name the service, version, strategy, deployment owner, rollback owner, decision window, expected customer impact, and the signals that can stop the release.

### 2. Prove serving readiness

A process being alive is not enough. Readiness should represent the ability to serve the intended traffic with required dependencies available. Liveness must not turn dependency degradation into a restart loop.

### 3. Protect compatibility

Old and new versions may overlap during rolling, Blue/Green, or canary deployment. Database schema, queue messages, cache entries, API contracts, feature flags, and background workers must remain compatible through that overlap and the rollback window.

### 4. Switch traffic using observable criteria

Validate the candidate environment before routing normal traffic. After the switch, watch error rate, p95/p99 latency, request rate, saturation, queue depth, database pressure, and a real customer transaction.

### 5. Keep reversal available

Retain the previous environment or artifact until the decision window closes. A rollback path that disappears immediately after traffic switch is not a reliable safety control.

## Strategy fit

| Strategy | Useful when | Primary operational risk |
|---|---|---|
| Rolling | Stateless or disruption-tolerant workloads | Bad readiness or capacity loss exposes broken instances. |
| Blue/Green | Critical web and API services needing fast reversal | Traffic switch, state, and environment drift are not validated. |
| Canary | Risky changes with strong telemetry | Metrics do not reveal customer impact quickly enough. |
| Feature flags | Behavior can be separated from deployment | Flags lack ownership, cleanup, or safe defaults. |
| Maintenance window | Legacy or tightly coupled systems | Calling downtime “zero downtime” hides the real customer plan. |

## Minimum release evidence

- service, version, image digest, chart or artifact identifier;
- deployment strategy and owners;
- readiness and graceful-shutdown validation;
- capacity and fault-domain state;
- migration and message compatibility decision;
- stop conditions and decision timestamps;
- traffic-switch and endpoint state;
- error, latency, saturation, queue, and database observations;
- critical business transaction result;
- rollback target and validation outcome;
- follow-up actions with owners and deadlines.

## Safety boundaries

- Do not use fixed example thresholds as universal SLOs.
- Do not combine irreversible schema removal with a release that may need rollback.
- Do not send traffic to a new environment before technical and business smoke checks pass.
- Do not remove the old environment before the agreed decision window closes.
- Do not retry unsafe, non-idempotent operations blindly during a partial rollout.
- Keep secrets, private endpoints, topology, and customer data out of public forks.
- Use an honest maintenance window when architecture cannot support a safe online change.

## Related SteadyOps resources

- Kubernetes rollback checklist: https://github.com/steadyops-best/kubernetes-rollback-checklist
- Disaster recovery runbook template: https://github.com/steadyops-best/disaster-recovery-runbook-template
- Kubernetes production-readiness guide: https://steadyops.best/articles/kubernetes-production-readiness-checklist/
- Kubernetes observability guide: https://steadyops.best/articles/kubernetes-observability-best-practices-for-sre-teams/
- Production reliability cases: https://steadyops.best/reliability-cases/

## Citation

GitHub can render citation metadata from [`CITATION.cff`](CITATION.cff). Retain the source repository and canonical guide when incorporating the checklist into an internal deployment standard.

## Contributing

Corrections and practical additions are welcome when they connect a real failure mode to a safe check, stop condition, rollback path, or validation step. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT. Use, adapt, and improve the checklist for your own deployment workflow. Production changes remain the responsibility of the team applying and validating it.