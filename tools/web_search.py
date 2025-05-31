"""DuckDuckGo web search tool."""

from duckduckgo_search import DDGS
from typing import List, Dict, Any


class WebSearchTool:
    """Web search tool using DuckDuckGo."""
    
    def __init__(self):
        self.ddgs = DDGS()
    
    def search(self, query: str, max_results: int = 3) -> List[Dict[str, Any]]:
        """Search the web for information."""
        try:
            results = list(self.ddgs.text(query, max_results=max_results))
            return [
                {
                    "title": result.get("title", ""),
                    "body": result.get("body", ""),
                    "url": result.get("href", "")
                }
                for result in results
            ]
        except Exception as e:
            return [{"error": f"Search failed: {str(e)}"}]
    
    def get_function_definition(self) -> Dict[str, Any]:
        """Get the function definition for the LLM."""
        return {
            "name": "web_search",
            "description": "Search the internet for current information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 3)",
                        "default": 3
                    }
                },
                "required": ["query"]
            }
        }


# Create a global instance
web_search_tool = WebSearchTool() 