"""Function definitions for tools available to the LLM."""

# Web search function definition
WEB_SEARCH_FUNCTION = {
    "name": "web_search",
    "description": "Search the internet for current information using DuckDuckGo",
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

# Wikipedia function definition (native LangChain tool)
WIKIPEDIA_FUNCTION = {
    "name": "wikipedia",
    "description": "Search Wikipedia for encyclopedic information about people, places, concepts, and historical events",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query for Wikipedia"
            }
        },
        "required": ["query"]
    }
}

# ArXiv function definition (native LangChain tool)
ARXIV_FUNCTION = {
    "name": "arxiv",
    "description": "Search arXiv for academic papers and research publications in science, mathematics, computer science, and other fields",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query for academic papers"
            }
        },
        "required": ["query"]
    }
}

# Python REPL function definition (native LangChain tool)
PYTHON_REPL_FUNCTION = {
    "name": "python_repl_ast",
    "description": "Execute Python code to perform complex calculations, data analysis, or programming tasks. Use for computational problems that require more than basic math.",
    "parameters": {
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "description": "Python code to execute"
            }
        },
        "required": ["command"]
    }
}

# Complete list of all available functions
ALL_FUNCTIONS = [
    # Custom tools
    WEB_SEARCH_FUNCTION,
    CALCULATOR_FUNCTION,
    DATETIME_FUNCTION,
    # Native LangChain tools
    WIKIPEDIA_FUNCTION,
    ARXIV_FUNCTION,
    PYTHON_REPL_FUNCTION
]

# Function descriptions for prompt inclusion
FUNCTION_DESCRIPTIONS = {
    # Custom tools
    "web_search": "Search the internet for current information using DuckDuckGo",
    "calculator": "Perform mathematical calculations with support for basic operations and parentheses",
    "get_datetime": "Get current date and time in various formats",
    # Native LangChain tools
    "wikipedia": "Search Wikipedia for encyclopedic information about people, places, concepts, and events",
    "arxiv": "Search arXiv for academic papers and research publications",
    "python_repl_ast": "Execute Python code for complex calculations, data analysis, or programming tasks"
} 