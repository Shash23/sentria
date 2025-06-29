from prometheus_api_client import PrometheusConnect

class PrometheusConnector:
    def __init__(self, prometheus_url: str):
        self.prometheus_url = prometheus_url
        self.prom = PrometheusConnect(url=self.prometheus_url, disable_ssl=True)

    def get_metric(self, metric_name: str, start_time: str, end_time: str, step: str):
        return self.prom.get_metric_range_data(
            metric_name=metric_name,
            start_time=start_time,
            end_time=end_time,
            step=step
        )

    def get_current_metric(self, metric_name: str):
        return self.prom.get_current_metric_value(metric_name=metric_name)

    def query(self, query: str, start_time: str = None, end_time: str = None):
        if start_time and end_time:
            return self.prom.query_range(query=query, start_time=start_time, end_time=end_time)
        return self.prom.query(query=query)