# Sentria Core README

## Overview

Sentria Core is the backend component of the Sentria project, designed to provide a robust API for handling observability queries and integrating with various telemetry sources. Built using FastAPI, it serves as the backbone for processing natural language queries and delivering actionable insights.

## Architecture

The architecture of Sentria Core consists of the following key components:

- **FastAPI**: The web framework used to build the API.
- **Routers**: Define the API endpoints for handling requests.
- **Services**: Contain the business logic for processing data and interacting with integrations.
- **Utilities**: Helper functions that support various functionalities within the application.

## Components

### 1. `src/main.py`
The entry point of the FastAPI application. It initializes the app, sets up middleware, and includes the routers.

### 2. `src/routers`
This directory contains route definitions for the API endpoints, allowing for organized and modular endpoint management.

### 3. `src/services`
Contains the core business logic and service functions that handle data processing and integration with telemetry sources.

### 4. `src/utils`
Utility functions that provide common functionalities used across the application.

## Setup Instructions

1. Clone the repository:

   git clone https://github.com/your-org/sentria.git

2. Navigate to the `sentria-core` directory:

   cd sentria-core

3. Install the required dependencies:

   pip install -r requirements.txt

4. Configure the environment variables in the `.env` file based on the `.env.example` provided.

5. Start the backend server:

   uvicorn main:app --reload

## Security Considerations

- Ensure that telemetry access is read-only.
- Implement scoped Role-Based Access Control (RBAC) for team- or service-level access.
- Consider optional Personally Identifiable Information (PII) scrubbing at ingestion.
- Query sessions should be isolated and auditable.

## Future Roadmap

- Enhance API security features.
- Implement additional telemetry integrations.
- Optimize performance for high-load scenarios.

## Tech Stack

- **Web Framework**: FastAPI (Python)
- **Database**: Depends on the chosen telemetry storage solution.
- **Authentication**: JWT or OAuth2 (to be determined).

## License

TBD — private for now. Open-core or MIT candidate in future.

## Maintainers

- Lead Architect: Shashwat Ghevde, MS Data Science
- Contributors: Open to collaborators post-MVP