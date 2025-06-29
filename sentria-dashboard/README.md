# Sentria Dashboard Component

This document provides an overview of the Sentria Dashboard component, detailing its purpose, functionality, and usage.

## Overview

The Sentria Dashboard component is responsible for generating dashboard specifications based on user intent. It translates user queries into actionable dashboard configurations that can be utilized in observability tools like Datadog and Grafana.

## Functionality

- **Dashboard Generation**: Converts user intent into JSON specifications for dashboards.
- **Chart Templates**: Provides templates for various chart types, including latency, throughput, error rates, and resource usage.
- **Utility Functions**: Contains helper functions to streamline the dashboard creation process.

## Usage

To use the Sentria Dashboard component, follow these steps:

1. **Import the Dashboard Generator**: Use the `dashboard_generator.py` to create dashboard specifications based on user queries.
2. **Utilize Chart Templates**: Access predefined chart templates from `chart_templates.py` to maintain consistency across dashboards.
3. **Leverage Utility Functions**: Use functions from `utils.py` to assist with common tasks related to dashboard generation.

## Example

Here’s a simple example of how to generate a dashboard specification:

```python
from src.dashboard_generator import generate_dashboard
from src.chart_templates import latency_chart_template

user_query = "Show me the latency for the /predict endpoint"
dashboard_spec = generate_dashboard(user_query, latency_chart_template)
```

## Dependencies

Ensure that the required dependencies are listed in the `requirements.txt` file and installed before running the component.

## Future Enhancements

- Integration with additional observability tools.
- Enhanced customization options for dashboard layouts.
- Support for real-time data updates in dashboards.

## License

This component is part of the Sentria project and follows the project's licensing terms.