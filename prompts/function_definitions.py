"""Function definitions for tools available to the LLM."""

# Web search function definition
WEB_SEARCH_FUNCTION = {
    "name": "web_search",
    "description": "Search the internet for current information",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query for web search"
            },
            "max_results": {
                "type": "integer",
                "description": "Maximum number of results (default: 3)",
                "default": 3
            }
        },
        "required": ["query"]
    }
}

# Calculator function definition
CALCULATOR_FUNCTION = {
    "name": "calculator",
    "description": "Perform mathematical calculations. Supports +, -, *, /, ** (power), and parentheses.",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "Mathematical expression to evaluate"
            }
        },
        "required": ["expression"]
    }
}

# DateTime function definition
DATETIME_FUNCTION = {
    "name": "get_datetime",
    "description": "Get current date and time information",
    "parameters": {
        "type": "object",
        "properties": {
            "format_type": {
                "type": "string",
                "description": "Format type: 'full', 'date', 'time', 'timestamp', or 'iso'",
                "default": "full"
            }
        },
        "required": []
    }
}

# Complete list of all available functions
ALL_FUNCTIONS = [
    WEB_SEARCH_FUNCTION,
    CALCULATOR_FUNCTION,
    DATETIME_FUNCTION
]

# Function descriptions for prompt inclusion
FUNCTION_DESCRIPTIONS = {
    "web_search": "Search the internet for current information using DuckDuckGo",
    "calculator": "Perform mathematical calculations with support for basic operations and parentheses",
    "get_datetime": "Get current date and time in various formats"
} 