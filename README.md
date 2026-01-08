## Sentria

Show estimated cloud cost impact in GitHub pull requests.

Sentria shows engineers the cloud cost impact of their code changes directly in pull requests.

When you open or merge a PR, Sentria analyzes the change and comments with the expected impact on your cloud bill before the cost reaches production.

---

## Problem

For growing tech companies, cloud costs are opaque and reactive.

Engineers ship code to improve performance or add features, but rarely see the cost implications of those changes until weeks later when the AWS bill arrives. Observability tools like Datadog can tell you when a service is slow or erroring, but they cannot tell you that a specific code change increased infrastructure costs by 30 percent.

As a result, teams either:
- Discover cost regressions too late, or
- Rely on manual FinOps analysis that is slow and disconnected from engineering workflows.

---

## Solution

Sentria brings cost awareness into the code review process.

By integrating with your Git provider, observability stack, and cloud billing data, Sentria attributes cloud cost changes to specific services and deployments and surfaces that information directly in pull requests.

Engineers can see the financial impact of a change before it is merged, making cost a first-class signal alongside performance and correctness.

---

## How It Works

1. **Pull Request Analysis**  
   Sentria monitors pull requests and detects changes that may affect infrastructure usage, such as scaling parameters, queries, caching behavior, or service configuration.

2. **Cost Attribution**  
   After deployment, Sentria correlates service-level metrics such as CPU, memory, request volume, and cache usage with cloud billing data to attribute cost changes to the affected services and deployments.

3. **PR Feedback**  
   Sentria posts a comment directly on the pull request with a clear cost summary.

   Example:
   > This change is estimated to increase Redis usage by approximately 40 percent, adding an estimated $600 per month.  
   > Primary driver: increased cache writes in `user-profile-service`.

   Or:
   > No significant cost impact detected. Resource utilization remains within baseline.

---

## Target Users

Sentria is built for engineering teams at small to mid-sized companies with meaningful cloud spend of $10,000 or more per month that do not have a dedicated FinOps team.

The primary buyer is the CTO or VP of Engineering, while the daily users are engineers and tech leads reviewing pull requests.

---

## Why Sentria

- **Cost awareness before merge**  
  Most tools explain costs after the money is spent. Sentria helps teams prevent unnecessary spend before it reaches production.

- **Built for engineers**  
  Sentria lives in pull requests, not finance dashboards. Engineers get cost context where decisions are made.

- **Clear ROI**  
  Teams pay for Sentria because it helps them avoid costly regressions and wasted infrastructure spend.

---

## Roadmap

Future capabilities include:
- Cost alerts for merged deployments
- Deeper attribution for multi-tenant systems
- Expansion into performance and reliability regressions tied to business impact
