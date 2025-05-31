"""Date and time tool."""

from datetime import datetime, timezone
from typing import Dict, Any


class DateTimeTool:
    """Tool for getting current date and time information."""
    
    def get_current_datetime(self, format_type: str = "full") -> str:
        """Get current date and time in various formats."""
        now = datetime.now(timezone.utc)
        
        if format_type == "date":
            return now.strftime("%Y-%m-%d")
        elif format_type == "time":
            return now.strftime("%H:%M:%S UTC")
        elif format_type == "timestamp":
            return str(int(now.timestamp()))
        elif format_type == "iso":
            return now.isoformat()
        else:  # full
            return now.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    def get_function_definition(self) -> Dict[str, Any]:
        """Get the function definition for the LLM."""
        return {
            "name": "get_datetime",
            "description": "Get current date and time information",
            "parameters": {
                "type": "object",
                "properties": {
                    "format_type": {
                        "type": "string",
                        "description": "Format type: 'full' (default), 'date', 'time', 'timestamp', or 'iso'",
                        "enum": ["full", "date", "time", "timestamp", "iso"],
                        "default": "full"
                    }
                },
                "required": []
            }
        }


# Create a global instance
datetime_tool = DateTimeTool() 