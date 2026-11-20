# Blue/Green traffic switching with a measurable stop decision

A green environment can respond to health checks while checkout, session handling, or background jobs fail under real traffic. Before the switch, write down what the owner will measure, when they can increase exposure, and how to get customers back to blue.

This example assumes a load balancer that supports traffic weights across two healthy environments. If your platform offers an all-at-once switch, use an isolated test route and explicit reversal criteria instead of copying the example percentages.

## Agree on the decision before serving users

1. **Name an owner and a customer action.** Choose something with an observable end result, such as a confirmation page for an order along with persisted order state. Use a safe test account or a synthetic operation designed for production.
2. **Record a blue baseline.** Capture a comparable window for the same path, including how many requests it served, failures, latency, and any queue delay. Check that the dashboard can separate blue from green.
3. **Set a minimum sample and a maximum hold.** Specify both how long to watch and how many requests you need. If traffic is too low before the maximum hold, keep exposure limited and decide explicitly whether to extend the window, drive safe synthetic checks, or return to blue.
4. **Rehearse reversal.** Verify blue still has capacity and can read what green writes. Name the owner who can restore routing, and define how to suspend green-only workers or features if they keep processing after traffic moves.

Traffic settings and connection behavior vary by load balancer. Check how sticky sessions and existing connections behave during reversal. For example, AWS Application Load Balancer does not automatically redirect weighted traffic away from an empty or unhealthy target group to a healthy group. [AWS listener actions documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-action-types.html)

## Example decision table

The numbers below are illustrative. Set the exposure, windows and limits using your own baseline, customer impact and capacity.

| Decision | Illustrative rule | Action |
|---|---|---|
| Advance | Green has served at least 200 checkout attempts over at least 10 minutes, failure rate is at most 1%, and the synthetic order reconciles | Increase exposure to the next agreed step. Open a new observation window. |
| Hold | Fewer than 200 attempts, missing per-environment telemetry, or decisions still depend on incomplete queue evidence | Keep the current weight, verify customer flow and resolve the evidence gap before moving on. |
| Reverse | At least two of the last 50 green checkout attempts fail for the release-related error, or any confirmed charge/order mismatch appears | Route new traffic back to blue and apply the agreed containment steps. Confirm exposure actually falls with routing telemetry. |

Reversal takes precedence over the hold or advance rule. Keep guardrail checks such as latency and background-job backlog in your release contract if the customer can be affected after the initial request.

## Worked release decision

At 10% exposure an illustrative green deployment served 60 checkout attempts. Two of the last 50 failed with the same new validation error. Blue served normal checkouts in the same window. The release owner applied the reversal rule without waiting for 200 attempts, restored blue routing, and confirmed that new requests were reaching blue. The owners then drained the green connections and reconciled the orders that had reached green before reversal.

Changing the traffic weight establishes the intended routing. Check the observed routing, run the customer action through the public entry point, and confirm callbacks or workers complete it. Keep blue available through the decision window even after a successful move to 100% green, until the owner has reviewed the post-switch evidence.

Copy the decision rules into the [deployment checklist](../checklist.md) and record observed counts, timestamps, and customer results in the [release evidence template](../release-evidence-template.md). See the [SteadyOps Blue/Green implementation guide](https://steadyops.best/articles/zero-downtime-bluegreen-deployments/) for traffic switching and migration compatibility together.
