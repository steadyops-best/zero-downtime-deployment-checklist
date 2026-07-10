# Zero-Downtime Deployment Checklist

Version: 1.0.0
Last reviewed: 2026-07-10

Implementation guide: https://steadyops.best/articles/zero-downtime-bluegreen-deployments/

## Release contract

- Service:
- Version:
- Strategy:
- Deployment owner:
- Rollback owner:
- Decision window:
- Customer-impact threshold:

## Readiness

- [ ] Health endpoint reflects real serving ability.
- [ ] Readiness prevents early traffic.
- [ ] Graceful shutdown and connection draining are tested.
- [ ] Workers can stop safely.
- [ ] Deployment timeout and stop conditions are defined.

## Observability

- [ ] Error rate and p95/p99 latency are visible.
- [ ] Request rate, saturation, queue depth, and dependencies are visible.
- [ ] Database connections and lock pressure are visible.
- [ ] Release version is visible in logs and dashboards.
- [ ] Critical user transaction is testable.

## Rollback

- [ ] Previous artifact or image digest is available.
- [ ] Rollback command is documented and tested.
- [ ] Database changes are backward-compatible.
- [ ] Rollback validation is defined.
- [ ] Decision owner is available.

## Traffic switch

- [ ] New environment passes technical smoke checks.
- [ ] New environment passes the critical business transaction.
- [ ] Router or ingress health behavior is verified.
- [ ] Connection draining is understood.
- [ ] Fast reversal is available.

## Post-deployment

- [ ] Error rate and latency remain within thresholds.
- [ ] Queue depth and database pressure are stable.
- [ ] Old environment remains available through the decision window.
- [ ] Rollback path is still valid.
- [ ] Release evidence and follow-up actions are recorded.
