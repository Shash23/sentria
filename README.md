## Sentria

Sentria is the AI FinOps analyst for engineering teams. It does not just say if your application is broken; it tells you where you are wasting money.

# Problem
For growing tech companies, the cloud bill is a blackbox. Engineers commonly deploy code and spin resources to improve performance and ship features, but are blind to the cost implications of their decisions. Observability platforms like Datadog can tell them if a service is slow but not that the fix they implemented increased their AWS bill by 30%. Companies either have to hire FinOps teams or deal with massive amounts of data regarding optimizing their cloud spend.

# Solution

Sentria is an AI platform that connects engineering telemetry to business outcomes. It allows engineers to understand and optimize their costs directly within their workflow. By integrating observability platforms (ie DataDog/Prometheus) and cloud billing providers (AWS Cost Explorer, GCP Billing), Sentria provides actionable financial insights. 

# How it Works

1. **Unified Data Ingestion**: Sentria connects to your existing tools. It pulls telemetries (metrics, traces, and logs) from your observability stack and correlates them with cost data from your cloud provider. 

2. **Proactive Cost Insights**: Sentria's AI proactively analyzes this combined data to find waste. It can send alerts directly to Slack or MS Teams. 

Example:
- "Alert: The user-profile-service is overprovisioned. It's running at 15% CPU utilization during peak hours. Downsizing the instance type could save ~$420/month with no performance impact."

- "Insight: Your latest deployment, v2.5.1, increased Redis commands by 300%, adding an estimated ~$600/month to your cache costs. Was this intended?"

3. **Natural Language Query for FinOps**: Engineers can ask questions like:

- "What's our most expensive API endpoint per customer
- "Show me the cost impact of the code deployed last Tuesday"
- Which of our tenants is costing us the most in database resouces?"

# Target Market

Small to mid-sized companies (10-250 employees) with significant cloud spend ($10k+ / month) that are too small for dedicated FinOps teams. The client is the CTO or VP of Engineering who is accountable for the cloud budget. 

# Key Differentiators

- **We sell a specific outcome**: cost savings. Our entire product is built to deliver a clear ROI.
- **Built for Engineers**: Traditional cost tools are for finance departments. Sentria is built for engineers who build the applications and provision resources to give them context to make cost-aware decisions. 
- **Focused Market**: By specializing in the niche of AI-powered cost optimization, we can build a better, more focused product than the general-purpose AI assistants from larger platforms. 

# Future Steps
- Expand into other outcome-driven analyses like performances or security