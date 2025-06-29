from typing import Any, Dict
import requests

class GrafanaConnector:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def get_dashboard(self, dashboard_uid: str) -> Dict[str, Any]:
        url = f"{self.base_url}/api/dashboards/uid/{dashboard_uid}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def query(self, query: str, start: int, end: int) -> Dict[str, Any]:
        url = f"{self.base_url}/api/ds/query"
        payload = {
            "queries": [
                {
                    "refId": "A",
                    "datasource": {"type": "prometheus", "uid": "prometheus"},
                    "rawSql": query,
                    "intervalMs": 1000,
                    "maxDataPoints": 1000,
                    "start": start,
                    "end": end
                }
            ]
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_alerts(self) -> Dict[str, Any]:
        url = f"{self.base_url}/api/alerts"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()