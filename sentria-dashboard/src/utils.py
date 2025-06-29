def generate_dashboard_spec(user_intent, metrics, logs, traces):
    dashboard_spec = {
        "title": f"Dashboard for {user_intent}",
        "charts": []
    }

    # Example chart for latency
    if "latency" in metrics:
        dashboard_spec["charts"].append({
            "type": "line",
            "title": "Latency Over Time",
            "data": metrics["latency"],
            "y_axis_label": "Latency (ms)"
        })

    # Example chart for error rates
    if "error_rate" in metrics:
        dashboard_spec["charts"].append({
            "type": "bar",
            "title": "Error Rate",
            "data": metrics["error_rate"],
            "y_axis_label": "Errors"
        })

    # Additional charts can be added based on user intent and available data
    return dashboard_spec

def format_chart_data(data):
    formatted_data = []
    for entry in data:
        formatted_data.append({
            "timestamp": entry["timestamp"],
            "value": entry["value"]
        })
    return formatted_data

def validate_dashboard_spec(dashboard_spec):
    required_keys = ["title", "charts"]
    for key in required_keys:
        if key not in dashboard_spec:
            raise ValueError(f"Missing required key: {key}")
    return True