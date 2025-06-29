from datadog import initialize, api

class DatadogConnector:
    def __init__(self, api_key, app_key):
        options = {
            'api_key': api_key,
            'app_key': app_key
        }
        initialize(**options)

    def get_metrics(self, metric_name, start, end, interval):
        return api.Metric.query(start=start, end=end, query=f'avg:{metric_name}{{*}}')

    def get_events(self, start, end):
        return api.Event.query(start=start, end=end)

    def get_service_checks(self, start, end):
        return api.ServiceCheck.query(start=start, end=end)

    def get_dashboard(self, dashboard_id):
        return api.Dashboard.get(dashboard_id)

    def create_event(self, title, text, tags=None):
        return api.Event.create(title=title, text=text, tags=tags)