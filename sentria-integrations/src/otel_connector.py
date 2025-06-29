from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

class OpenTelemetryConnector:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key

    def get_metrics(self):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{self.endpoint}/v1/metrics', headers=headers)
        return response.json() if response.status_code == 200 else None

    def get_traces(self):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{self.endpoint}/v1/traces', headers=headers)
        return response.json() if response.status_code == 200 else None

    def get_logs(self):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.get(f'{self.endpoint}/v1/logs', headers=headers)
        return response.json() if response.status_code == 200 else None

@app.route('/otel/metrics', methods=['GET'])
def fetch_metrics():
    connector = OpenTelemetryConnector(endpoint='https://your-otel-endpoint', api_key='your-api-key')
    metrics = connector.get_metrics()
    return jsonify(metrics)

@app.route('/otel/traces', methods=['GET'])
def fetch_traces():
    connector = OpenTelemetryConnector(endpoint='https://your-otel-endpoint', api_key='your-api-key')
    traces = connector.get_traces()
    return jsonify(traces)

@app.route('/otel/logs', methods=['GET'])
def fetch_logs():
    connector = OpenTelemetryConnector(endpoint='https://your-otel-endpoint', api_key='your-api-key')
    logs = connector.get_logs()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)