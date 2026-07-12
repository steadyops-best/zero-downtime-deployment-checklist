# Production Release Evidence Record

Version: 1.0.0  
Canonical guide: https://steadyops.best/articles/zero-downtime-bluegreen-deployments/

Complete this record for a production deployment or production-like release exercise. Store it with pipeline logs, approvals, dashboards, and follow-up work.

## Release identity

- Service:
- Environment:
- Version:
- Image digest/artifact:
- Commit SHA:
- Deployment strategy:
- Deployment owner:
- Rollback owner:
- Change/release ticket:
- Decision window:

## Release contract

- Expected customer impact:
- Critical customer transaction:
- Error-rate stop condition:
- Latency stop condition:
- Saturation/capacity stop condition:
- Queue or worker stop condition:
- Database stop condition:
- Maximum deployment duration:

## Compatibility review

| Area | Compatible during overlap and rollback? | Evidence/notes |
|---|---|---|
| Database schema | | |
| Queue/message format | | |
| API contract | | |
| Cache/session format | | |
| Feature flags/config | | |
| Background workers | | |
| Secrets/credentials | | |

## Pre-release evidence

- [ ] Previous artifact and rollback target are available.
- [ ] Readiness reflects real serving ability.
- [ ] Graceful shutdown and connection draining were tested.
- [ ] Required capacity and fault-domain state are healthy.
- [ ] Monitoring shows release version and critical signals.
- [ ] Technical and business smoke tests are ready.
- [ ] Rollback command and decision authority are known.

## Deployment and traffic timeline

| UTC time | Owner | Event/action | Expected result | Actual result | Evidence |
|---|---|---|---|---|---|
| | | Deployment started | | | |
| | | Candidate environment ready | | | |
| | | Technical smoke passed | | | |
| | | Business smoke passed | | | |
| | | Traffic switch started | | | |
| | | Traffic switch completed | | | |
| | | Decision window completed | | | |

## Production signals

| Signal | Baseline/target | Candidate result | After traffic switch | Final result |
|---|---|---|---|---|
| Error rate | | | | |
| p95 latency | | | | |
| p99 latency | | | | |
| Request rate | | | | |
| CPU/memory saturation | | | | |
| Queue depth/drain time | | | | |
| Database connections/locks | | | | |
| Dependency errors | | | | |

## Traffic and business validation

- Router/ingress/load balancer state:
- Candidate endpoints:
- Old environment state:
- Connection-draining result:
- Critical transaction:
- Test owner:
- Test result:
- Evidence:

## Rollback readiness after switch

- [ ] Previous environment/artifact is still available.
- [ ] Database and messages remain backward-compatible.
- [ ] Reversal command or traffic action remains valid.
- [ ] Rollback validation steps remain executable.
- [ ] Rollback owner remains available through the decision window.

## Final outcome

- Release successful: yes/no/partial
- Customer impact:
- Deployment duration:
- Decision-window result:
- Rollback used: yes/no
- Remaining risk:
- Monitoring window completed:

## Follow-up actions

| Action | Risk addressed | Owner | Deadline | Verification |
|---|---|---|---|---|
| | | | | |

## Review

- Record reviewed by:
- Review date:
- Checklist/runbook updates required:
- Next release exercise: