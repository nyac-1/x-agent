"""LangChain-compatible tools for the agent."""

from typing import Optional, Type
from langchain_core.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field

# Import custom tools
from .web_search import web_search_tool
from .calculator import calculator_tool  
from .datetime_tool import datetime_tool

# Import native LangChain tools
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
from langchain_experimental.tools import PythonREPLTool


# Custom tool wrappers (existing)
class WebSearchInput(BaseModel):
    """Input for web search tool."""
    query: str = Field(description="Search query for web search")
    max_results: int = Field(default=3, description="Maximum number of results")


class WebSearchTool(BaseTool):
    """LangChain web search tool."""
    name: str = "web_search"
    description: str = "Search the internet for current information using DuckDuckGo"
    args_schema: Type[BaseModel] = WebSearchInput

    def _run(
        self, 
        query: str, 
        max_results: int = 3,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Execute web search."""
        results = web_search_tool.search(query, max_results)
        
        # Format results for LangChain
        if not results or (len(results) == 1 and "error" in results[0]):
            return f"Search failed: {results[0].get('error', 'Unknown error')}"
        
        formatted_results = []
        for result in results:
            formatted_results.append(
                f"Title: {result.get('title', 'N/A')}\n"
                f"Content: {result.get('body', 'N/A')}\n"
                f"URL: {result.get('url', 'N/A')}\n"
            )
        
        return "\n---\n".join(formatted_results)


class CalculatorInput(BaseModel):
    """Input for calculator tool."""
    expression: str = Field(description="Mathematical expression to evaluate")


class CalculatorTool(BaseTool):
    """LangChain calculator tool."""
    name: str = "calculator"
    description: str = "Perform mathematical calculations. Supports +, -, *, /, ** (power), and parentheses."
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(
        self, 
        expression: str,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Execute calculation."""
        result = calculator_tool.calculate(expression)
        return f"Result: {result}"


class DateTimeInput(BaseModel):
    """Input for datetime tool."""
    format_type: str = Field(
        default="full", 
        description="Format type: 'full', 'date', 'time', 'timestamp', or 'iso'"
    )


class DateTimeTool(BaseTool):
    """LangChain datetime tool."""
    name: str = "get_datetime"
    description: str = "Get current date and time information"
    args_schema: Type[BaseModel] = DateTimeInput

    def _run(
        self, 
        format_type: str = "full",
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Get current datetime."""
        result = datetime_tool.get_current_datetime(format_type)
        return f"Current datetime ({format_type}): {result}"


# Create custom tool instances
langchain_web_search = WebSearchTool()
langchain_calculator = CalculatorTool()  
langchain_datetime = DateTimeTool()

# Create native LangChain tool instances
wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
arxiv_tool = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())
python_repl_tool = PythonREPLTool()

# Configure tool descriptions for better agent understanding
wikipedia_tool.description = "Search Wikipedia for encyclopedic information about people, places, concepts, and historical events"
arxiv_tool.description = "Search arXiv for academic papers and research publications in science, mathematics, computer science, and other fields"
python_repl_tool.description = "Execute Python code to perform complex calculations, data analysis, or programming tasks. Use for computational problems that require more than basic math."

# Export all tools list
LANGCHAIN_TOOLS = [
    # Custom tools
    langchain_web_search,
    langchain_calculator,
    langchain_datetime,
    # Native LangChain tools  
    wikipedia_tool,
    arxiv_tool,
    python_repl_tool
] 