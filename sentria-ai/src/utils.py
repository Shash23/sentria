def generate_prompt(template, context):
    """
    Generates a prompt for the LLM based on the provided template and context.

    Args:
        template (str): The prompt template to use.
        context (dict): A dictionary containing context information.

    Returns:
        str: The generated prompt.
    """
    return template.format(**context)

def extract_relevant_data(logs, metrics, traces, alerts):
    """
    Extracts relevant data from logs, metrics, traces, and alerts.

    Args:
        logs (list): A list of log entries.
        metrics (list): A list of metric entries.
        traces (list): A list of trace entries.
        alerts (list): A list of alert entries.

    Returns:
        dict: A dictionary containing the extracted relevant data.
    """
    relevant_data = {
        "logs": logs,
        "metrics": metrics,
        "traces": traces,
        "alerts": alerts
    }
    return relevant_data

def format_response(summary, root_cause, remediation):
    """
    Formats the response to be returned to the user.

    Args:
        summary (str): A summary of the issue.
        root_cause (str): The identified root cause.
        remediation (str): Suggested remediation steps.

    Returns:
        dict: A formatted response dictionary.
    """
    return {
        "summary": summary,
        "root_cause": root_cause,
        "remediation": remediation
    }