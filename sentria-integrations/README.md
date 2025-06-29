# Sentria Integrations

**Overview**

The Sentria Integrations component is responsible for connecting to various telemetry data sources, including Datadog, Grafana, Prometheus, Loki, and OpenTelemetry. This component normalizes the data collected from these sources into a unified schema, enabling seamless interaction with the Sentria platform.

---

## Features

- **Datadog Connector**: Interface for fetching metrics and logs from the Datadog API.
- **Grafana Connector**: Interface for retrieving data from Grafana, including support for Prometheus and Loki.
- **Prometheus Connector**: Fetches metrics from Prometheus for real-time monitoring.
- **Loki Connector**: Integrates with Loki for log aggregation and querying.
- **OpenTelemetry Connector**: Interfaces with OpenTelemetry Collector to gather telemetry data.

---

## Setup Instructions

1. **Install Dependencies**: Navigate to the `sentria-integrations` directory and install the required Python packages listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

2. **Configuration**: Ensure that the necessary API keys and configuration settings are provided in the environment variables or configuration files as needed.

---

## Usage

Each connector can be imported and used to fetch data from the respective telemetry source. For example:

```python
from sentria_integrations.datadog_connector import DatadogConnector

datadog = DatadogConnector(api_key='your_api_key')
metrics = datadog.get_metrics()
```

---

## Contributing

Contributions are welcome! Please follow the standard procedure for submitting pull requests and ensure that your code adheres to the project's coding standards.

---

## License

This project is currently private. Future plans may include transitioning to an open-core or MIT license.

---

## Maintainers

- Shashwat Ghevde, MS Data Science (Lead Architect)
- Contributors: Open to collaborators post-MVP