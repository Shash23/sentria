from typing import Any, Dict
import requests

class LokiConnector:
    def __init__(self, base_url: str, username: str = None, password: str = None):
        self.base_url = base_url
        self.username = username
        self.password = password

    def query(self, query: str, start: str, end: str) -> Dict[str, Any]:
        """
        Query Loki for logs based on the provided query string and time range.

        :param query: The log query string.
        :param start: Start time in RFC3339 format.
        :param end: End time in RFC3339 format.
        :return: The response from the Loki API.
        """
        url = f"{self.base_url}/loki/api/v1/query_range"
        params = {
            'query': query,
            'start': start,
            'end': end
        }
        response = requests.get(url, params=params, auth=(self.username, self.password) if self.username and self.password else None)
        response.raise_for_status()
        return response.json()

    def health_check(self) -> Dict[str, Any]:
        """
        Check the health of the Loki instance.

        :return: The health status of the Loki API.
        """
        url = f"{self.base_url}/loki/api/v1/health"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()