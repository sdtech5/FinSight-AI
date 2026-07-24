# Import the tool decorator
from langchain_core.tools import tool
from langchain_tavily import TavilySearch


# Calculator tool
@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example: "25 * 4"
    """
    return str(eval(expression))


# Tavily web search tool
search_web = TavilySearch(max_results=3)


# List of available tools
tools = [calculator,search_web]