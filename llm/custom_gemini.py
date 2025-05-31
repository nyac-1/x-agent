"""Custom Gemini LLM with exactly 3 methods and rate limiting."""

import time
import json
import google.generativeai as genai
from typing import List, Dict, Any
from prompts.schemas import FUNCTION_CALL_SCHEMA


class CustomGeminiLLM:
    """Custom Gemini LLM wrapper with exactly 3 methods."""
    
    def __init__(self, api_key: str):
        """Initialize the Gemini LLM with API key."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def text_to_text(self, prompt: str) -> str:
        """
        Basic text completion method.
        
        Args:
            prompt: Input text prompt
            
        Returns:
            Generated text response
        """
        try:
            # Rate limiting - 1 second between calls
            time.sleep(1)
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error in text_to_text: {str(e)}"
    
    def text_to_json(self, prompt: str, schema: dict) -> dict:
        """
        Generate structured JSON response.
        
        Args:
            prompt: Input text prompt
            schema: JSON schema for validation
            
        Returns:
            Structured JSON response
        """
        try:
            # Rate limiting - 1 second between calls
            time.sleep(1)
            
            # Enhanced prompt for JSON generation
            json_prompt = f"""
{prompt}

Please respond with valid JSON that matches this schema:
{json.dumps(schema, indent=2)}

Response (JSON only):
"""
            
            response = self.model.generate_content(json_prompt)
            
            # Try to parse JSON
            try:
                return json.loads(response.text)
            except json.JSONDecodeError:
                # If JSON parsing fails, return error structure
                return {
                    "error": "Failed to parse JSON response",
                    "raw_response": response.text
                }
                
        except Exception as e:
            return {
                "error": f"Error in text_to_json: {str(e)}"
            }
    
    def text_to_function_call(self, prompt: str, functions: List[dict]) -> dict:
        """
        Generate function call in Vertex AI style.
        
        Args:
            prompt: Input text prompt
            functions: List of available function definitions
            
        Returns:
            Function call specification
        """
        try:
            # Rate limiting - 1 second between calls
            time.sleep(1)
            
            # Create function calling prompt
            functions_text = json.dumps(functions, indent=2)
            function_prompt = f"""
{prompt}

Available functions:
{functions_text}

If you need to call a function, respond with JSON matching this schema:
{json.dumps(FUNCTION_CALL_SCHEMA, indent=2)}

If no function is needed, respond with:
{{"function_name": null, "parameters": null}}

Response (JSON only):
"""
            
            response = self.model.generate_content(function_prompt)
            
            # Try to parse JSON
            try:
                result = json.loads(response.text)
                return result
            except json.JSONDecodeError:
                return {
                    "function_name": None,
                    "parameters": None,
                    "error": "Failed to parse function call response",
                    "raw_response": response.text
                }
                
        except Exception as e:
            return {
                "function_name": None,
                "parameters": None,
                "error": f"Error in text_to_function_call: {str(e)}"
            }


if __name__ == "__main__":
    # Test the custom LLM (requires GEMINI_API_KEY environment variable)
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if api_key:
        llm = CustomGeminiLLM(api_key)
        
        # Test text_to_text
        print("Testing text_to_text:")
        result = llm.text_to_text("What is the capital of France?")
        print(f"Result: {result}")
        
        # Test text_to_json
        print("\nTesting text_to_json:")
        schema = {"type": "object", "properties": {"capital": {"type": "string"}}}
        result = llm.text_to_json("What is the capital of France?", schema)
        print(f"Result: {result}")
        
        # Test text_to_function_call
        print("\nTesting text_to_function_call:")
        functions = [{
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"]
            }
        }]
        result = llm.text_to_function_call("What's the weather in Paris?", functions)
        print(f"Result: {result}")
    else:
        print("GEMINI_API_KEY not found") 