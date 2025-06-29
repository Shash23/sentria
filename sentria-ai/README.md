# FILE: /sentria/sentria/sentria-ai/README.md

# Sentria AI Component

**Overview**

The Sentria AI component is responsible for implementing the retrieval-augmented generation (RAG) and large language model (LLM) pipeline. It leverages advanced AI techniques to provide insightful responses to user queries based on telemetry data.

---

## What It Does

- Implements a pipeline that combines RAG with LLMs to generate human-like responses.
- Utilizes prompt templates to guide the LLM in producing relevant and concise outputs.
- Integrates with the telemetry retriever to access indexed telemetry data for enhanced query responses.

---

## Key Files

### 1. `llm_pipeline.py`
- Contains the core logic for the RAG and LLM pipeline.
- Manages the interaction between the LLM and the telemetry data.

### 2. `prompt_templates.py`
- Defines various prompt templates used to structure queries to the LLM.
- Ensures that the LLM receives contextually relevant information for generating responses.

### 3. `utils.py`
- Provides utility functions that support the AI component's operations.
- Includes functions for data preprocessing and formatting.

---

## Setup Instructions

1. Navigate to the `sentria-ai` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure that the environment is configured to access the necessary APIs and services.

---

## Future Enhancements

- Explore additional LLMs for improved response quality.
- Implement user feedback mechanisms to refine AI responses.
- Expand the range of prompt templates for diverse query types.

---

## License

TBD — private for now. Open-core or MIT candidate in future.

---

## Maintainers

Lead Architect: Shashwat Ghevde, MS Data Science

Contributors: Open to collaborators post-MVP