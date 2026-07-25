# Import the tool decorator
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
import yfinance as yf


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

# Yahoo finance tool
@tool
def finance_tool(symbol: str) -> str:
    """
    Fetches the latest stock information from Yahoo Finance.

    Example:
    RELIANCE.NS
    TCS.NS
    INFY.NS
    """

    try:
        ticker = yf.Ticker(symbol)

        info = ticker.fast_info

        return f"""
            Symbol: {symbol}
            Current Price: ₹{round(info.get("lastPrice", 0), 2)}
            Day High: ₹{round(info.get("dayHigh", 0), 2)}
            Day Low: ₹{round(info.get("dayLow", 0), 2)}
            Previous Close: ₹{round(info.get("previousClose", 0), 2)}
            """

    except Exception as e:
        return f"Error fetching stock data: {e}"


# List of available tools
tools = [calculator,search_web,finance_tool]