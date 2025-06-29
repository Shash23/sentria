from typing import Dict, List

def get_prompt_templates() -> Dict[str, List[str]]:
    return {
        "default": [
            "User: {user_query}\nContext:\n- Logs: {logs}\n- Metrics: {metrics}\n- Traces: {traces}\n- Alerts: {alerts}\nGenerate: Summary of issue + root cause + remediation suggestion.",
        ],
        "latency_spike": [
            "User: 'Why did inference latency spike last night?'\nContext:\n- Logs: {logs}\n- Metrics: {metrics}\n- Traces: {traces}\n- Alerts: {alerts}\nGenerate: Summary of issue + root cause + remediation suggestion.",
        ],
        "error_analysis": [
            "User: 'What caused the 500 errors in the last hour?'\nContext:\n- Logs: {logs}\n- Metrics: {metrics}\n- Traces: {traces}\n- Alerts: {alerts}\nGenerate: Summary of issue + root cause + remediation suggestion.",
        ],
        "endpoint_performance": [
            "User: 'Why was the {endpoint} slow yesterday?'\nContext:\n- Logs: {logs}\n- Metrics: {metrics}\n- Traces: {traces}\n- Alerts: {alerts}\nGenerate: Summary of issue + root cause + remediation suggestion.",
        ],
    }