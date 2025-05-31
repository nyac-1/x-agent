"""Custom Gemini LLM wrapper with exactly 3 methods."""

import json
import time
from typing import List, Dict, Any
import google.generativeai as genai
from .schemas import TOOL_SELECTION_SCHEMA, FUNCTION_CALL_SCHEMA


class CustomGeminiLLM:
    """Custom Gemini LLM wrapper with exactly 3 operations."""
    
    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """Initialize the Gemini LLM wrapper."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.sleep_duration = 1  # 1 second sleep between requests
    
    def _make_request(self, prompt: str) -> str:
        """Make a request to Gemini with rate limiting."""
        time.sleep(self.sleep_duration)
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")
    
    def text_to_text(self, prompt: str) -> str:
        """Basic text completion."""
        return self._make_request(prompt)
    
    def text_to_json(self, prompt: str, schema: dict) -> dict:
        """Structured JSON response."""
        structured_prompt = f"""
{prompt}

Respond ONLY in valid JSON format matching this exact schema:
{json.dumps(schema, indent=2)}

Important: Your response must be valid JSON that can be parsed. Do not include any text before or after the JSON.
"""
        response_text = self._make_request(structured_prompt)
        
        # Clean up response and parse JSON
        try:
            # Remove any potential markdown formatting
            if response_text.startswith("```json"):
                response_text = response_text.replace("```json", "").replace("```", "").strip()
            elif response_text.startswith("```"):
                response_text = response_text.replace("```", "").strip()
            
            return json.loads(response_text)
        except json.JSONDecodeError as e:
            # Fallback: try to extract JSON from the response
            try:
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                if start != -1 and end != 0:
                    json_part = response_text[start:end]
                    return json.loads(json_part)
            except:
                pass
            raise Exception(f"Failed to parse JSON response: {str(e)}\nResponse: {response_text}")
    
    def text_to_function_call(self, prompt: str, functions: List[dict]) -> dict:
        """Function calling (Vertex AI style)."""
        function_prompt = f"""
{prompt}

Available functions:
{json.dumps(functions, indent=2)}

Based on the context and available functions, determine which function to call and with what parameters.

Respond in JSON format:
{{
    "function_name": "name_of_function_to_call",
    "parameters": {{
        "param1": "value1",
        "param2": "value2"
    }}
}}

If no function call is needed, respond with:
{{
    "function_name": null,
    "parameters": {{}}
}}
"""
        return self.text_to_json(function_prompt, FUNCTION_CALL_SCHEMA) 