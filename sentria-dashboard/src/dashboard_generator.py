def generate_dashboard_spec(user_intent):
    """
    Generates a dashboard specification based on user intent.

    Args:
        user_intent (str): The user's request or intent for the dashboard.

    Returns:
        dict: A dictionary representing the dashboard specification.
    """
    dashboard_spec = {
        "title": f"Dashboard for {user_intent}",
        "widgets": []
    }

    # Example logic to determine widgets based on user intent
    if "latency" in user_intent:
        dashboard_spec["widgets"].append({
            "type": "line_chart",
            "title": "Latency Over Time",
            "data_source": "latency_metrics",
            "x_axis": "time",
            "y_axis": "latency_ms"
        })

    if "error" in user_intent:
        dashboard_spec["widgets"].append({
            "type": "bar_chart",
            "title": "Error Rate",
            "data_source": "error_metrics",
            "x_axis": "time",
            "y_axis": "error_count"
        })

    return dashboard_spec


def convert_to_json_spec(dashboard_spec):
    """
    Converts the dashboard specification to JSON format.

    Args:
        dashboard_spec (dict): The dashboard specification.

    Returns:
        str: A JSON string representation of the dashboard specification.
    """
    import json
    return json.dumps(dashboard_spec, indent=4)