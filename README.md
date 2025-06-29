# Sentria

**AI-powered observability assistant for non-SRE engineers.**

Sentria is a platform that lets any engineer query system behavior using plain English — and get back clear, actionable explanations, incident summaries, and dashboards based on real telemetry data (logs, traces, and metrics). Built for ML engineers, data engineers, and developers who want insight without needing to master Datadog or Grafana.

---

## What It Does

- Ask natural-language questions like:
  - “Why was the /predict endpoint slow yesterday?”
  - “What caused 500 errors in the last hour?”
- Automatically pulls data from telemetry sources:
  - Datadog, Grafana, Prometheus, and OpenTelemetry
- Uses Retrieval-Augmented Generation (RAG) and LLMs to:
  - Summarize anomalies
  - Suggest root causes and remediations
  - Create or recommend dashboards

---

## Use Case Example

**ML Engineer**: “Why did inference latency spike last night?”

**Sentria responds**:
- “At 2:13 AM, P95 latency increased to 1.9s. Pod node-4 hit 97% CPU. Autoscaling was delayed due to throttling limits. Suggest increasing warm-start buffer.”

---

## Architecture Overview

[User] → [Chat UI] → [Query Engine]
├─→ [LLM w/ RAG]
└─→ [Dashboard Generator]
└─→ [Telemetry APIs: Datadog, Grafana, OTel]

---

## Components

### 1. `sentria-ui`
- React-based web chat interface
- Accepts natural language queries and displays responses, charts, dashboards

### 2. `sentria-core`
- FastAPI backend for routing queries, integrating services
- Handles authentication, logging, and tracing

### 3. `sentria-integrations`
- Connectors for:
  - Datadog API
  - Grafana API / Prometheus / Loki
  - OpenTelemetry Collector
- Normalizes metrics/logs/traces into a unified schema

### 4. `sentria-retriever`
- Indexes telemetry chunks into a vector database (Qdrant or Weaviate)
- Used for retrieval-augmented generation (RAG) over logs, metrics, and traces

### 5. `sentria-ai`
- RAG + LLM pipeline using GPT-4, Claude, or Mixtral
- Prompt templates guide the LLM to produce concise, explainable output

### 6. `sentria-dashboard`
- Converts user intent into dashboard JSON specs
- Supports Datadog and Grafana dashboard generation
- Includes charts like latency, throughput, error rate, CPU/memory, etc.

---

## Example Telemetry Schema

### Metric

{
  "service": "ml-api",
  "endpoint": "/predict",
  "metric": "latency_p95",
  "unit": "ms",
  "timestamp": "2025-06-29T14:00:00Z",
  "value": 1203
}

### Log

{
  "level": "error",
  "service": "ml-api",
  "message": "OOMKilled on node-3",
  "timestamp": "2025-06-29T13:58:00Z"
}

### Trace

{
  "trace_id": "abc123",
  "span": "/predict",
  "duration_ms": 3200,
  "status": "error",
  "resource": "pod-xyz"
}

---

## Setup Instructions

1. Clone the repo:
   git clone https://github.com/your-org/sentria.git

2. Install backend dependencies:
   cd sentria-core
   pip install -r requirements.txt

3. Configure .env with API keys for:
   - Datadog
   - Grafana / Prometheus
   - OpenTelemetry Collector
   - OpenAI or Claude or Mixtral

4. Start backend server:
   uvicorn main:app --reload

5. Run telemetry retriever:
   python retriever/index_telemetry.py

6. Launch the frontend:
   cd sentria-ui
   npm install
   npm run dev

---

## Security Considerations

- Telemetry access is read-only
- Supports scoped RBAC for team- or service-level access
- Optional PII scrubbing at ingestion
- Query sessions are isolated and auditable

---

## Future Roadmap

- Slack and Teams chatbot integrations
- Post-incident AI-generated summaries
- Cost anomaly detection
- GitOps remediation suggestions
- Role-based dashboard generation

---

## Tech Stack

| Layer            | Technology                       |
|------------------|----------------------------------|
| UI               | React + Tailwind                 |
| API Gateway      | FastAPI (Python)                |
| Retrieval        | Qdrant or Weaviate              |
| LLM Engine       | LangChain or LlamaIndex         |
| Vectorizer       | OpenAI embeddings or BGE         |
| Logs/Traces      | OpenTelemetry + Loki             |
| Dashboards       | Datadog, Grafana JSON APIs      |
| Hosting          | Vercel / Render / Railway        |

---

## Project Name

Sentria  
Tagline: “System clarity, without the complexity.”  
Suggested domain: sentria.dev or sentria.ai

---

## License

TBD — private for now. Open-core or MIT candidate in future.

---

## Maintainers

Lead Architect: Shashwat Ghevde
Contributors: Open to collaborators post-MVP