"""JSON schemas for structured LLM responses."""

TOOL_SELECTION_SCHEMA = {
    "type": "object",
    "properties": {
        "needs_tools": {
            "type": "boolean",
            "description": "Whether tools are needed to answer the question"
        },
        "reasoning": {
            "type": "string",
            "description": "Explanation of why tools are or aren't needed"
        },
        "tools_needed": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of tool names needed (empty if no tools needed)"
        },
        "direct_answer": {
            "type": ["string", "null"],
            "description": "Direct answer if no tools are needed, null otherwise"
        }
    },
    "required": ["needs_tools", "reasoning", "tools_needed", "direct_answer"]
}

FUNCTION_CALL_SCHEMA = {
    "type": "object",
    "properties": {
        "function_name": {
            "type": "string",
            "description": "Name of the function to call"
        },
        "parameters": {
            "type": "object",
            "description": "Parameters to pass to the function"
        }
    },
    "required": ["function_name", "parameters"]
} 