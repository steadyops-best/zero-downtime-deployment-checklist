# Contributing

Contributions should improve release safety, rollback clarity, compatibility, observability, or validation for real production changes.

## Good contributions

- Add a missing readiness, graceful-shutdown, capacity, or traffic-draining check.
- Clarify rolling, Blue/Green, canary, feature-flag, Helm, Kubernetes, or ingress behavior.
- Improve database migration, queue-message, cache, or API compatibility guidance.
- Add a stop condition or rollback validation step tied to customer impact.
- Correct commands and link to primary documentation.
- Improve release-evidence fields and ownership requirements.

## Avoid

- Secrets, internal endpoints, customer data, or private topology.
- Fixed thresholds presented as universal production values.
- Destructive migration advice without a compatibility and rollback plan.
- Vendor marketing, copied product claims, or unrelated SEO links.
- Calling a strategy zero-downtime without explaining readiness, traffic, state, and reversal behavior.
- Commands that change production without review, expected results, and validation.

## Change format

A useful proposal should explain:

1. the failure mode or release gap;
2. the deployment strategies it affects;
3. the proposed checklist change;
4. the stop or rollback condition;
5. the technical and business validation method;
6. compatibility or capacity risks;
7. the evidence that should be retained.

Use safe placeholders rather than real service names, domains, tokens, or account identifiers.

## Source and canonical guide

The reusable checklist lives here. The maintained explanatory guide is:

https://steadyops.best/articles/zero-downtime-bluegreen-deployments/

Material changes to the release-safety model should keep the repository and canonical guide consistent.