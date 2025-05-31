"""LangChain adapter for the custom 3-method Gemini LLM."""

from typing import Any, Dict, List, Optional
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from pydantic import Field
from .custom_gemini import CustomGeminiLLM


class LangChainGeminiAdapter(LLM):
    """LangChain-compatible wrapper for CustomGeminiLLM."""
    
    custom_llm: CustomGeminiLLM = Field(default=None, exclude=True)
    api_key: str = Field(default=None, exclude=True)
    
    def __init__(self, api_key: str, **kwargs):
        super().__init__(api_key=api_key, **kwargs)
        self.custom_llm = CustomGeminiLLM(api_key)
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Standard LangChain _call method using our custom LLM."""
        return self.custom_llm.text_to_text(prompt)
    
    @property
    def _llm_type(self) -> str:
        """Return LLM type for LangChain."""
        return "custom_gemini"
    
    @property 
    def _identifying_params(self) -> Dict[str, Any]:
        """Return identifying parameters."""
        return {"model_name": "custom_gemini_3_method"}
    
    # Expose custom methods for direct access when needed
    def get_structured_response(self, prompt: str, schema: dict) -> dict:
        """Get structured JSON response using text_to_json."""
        return self.custom_llm.text_to_json(prompt, schema)
    
    def get_function_call(self, prompt: str, functions: List[dict]) -> dict:
        """Get function call decision using text_to_function_call."""
        return self.custom_llm.text_to_function_call(prompt, functions) 