from fastapi import HTTPException
from typing import Any, Dict
import openai

class LLM:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_response(self, prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

class LLM_Pipeline:
    def __init__(self, llm: LLM):
        self.llm = llm

    def process_query(self, query: str, context: Dict[str, Any]) -> str:
        prompt = self.create_prompt(query, context)
        return self.llm.generate_response(prompt)

    def create_prompt(self, query: str, context: Dict[str, Any]) -> str:
        context_str = "\n".join([f"{key}: {value}" for key, value in context.items()])
        return f"User Query: {query}\nContext:\n{context_str}\nGenerate a concise and actionable response."