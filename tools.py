from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from datetime import datetime

search_tool = DuckDuckGoSearchRun()


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example:
    calculator("25 * 8")
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Error: {str(e)}"
    
@tool
def date() -> str:
    """
    Returns the current date and time. Use this whenever the user asks for the current time or date.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

@tool
def get_time() -> str:
    """Returns current time."""
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")



tools = [search_tool,date,calculator,get_time]


