"""Tool definitions for the AI Agent Explorer Learning Lab.

This module demonstrates how "tools" are simply Python functions
decorated with @tool. The LLM receives descriptions of these functions
and can call them during conversation.
"""

from datetime import datetime
import math
from smolagents import tool


@tool
def magic_calculator(expression: str) -> str:
    """Evaluate mathematical expressions safely.

    This tool can perform basic arithmetic operations and common mathematical
    functions. It evaluates Python expressions in a safe, controlled environment.

    Args:
        expression: A mathematical expression as a string (e.g., "2 + 2", "sqrt(16)", "3 * 7 + 1")

    Returns:
        The result of the mathematical expression as a string.

    Examples:
        - "2 + 2" returns "4"
        - "sqrt(16)" returns "4.0"
        - "3 * 7 + 1" returns "22"
    """
    try:
        # Safe evaluation using math module
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        allowed_names.update({"abs": abs, "round": round, "min": min, "max": max})
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error calculating expression: {str(e)}"


@tool
def time_checker() -> str:
    """Get the current date and time.

    This tool returns the current system time in a human-readable format.
    Useful for answering questions about what time it is, what day it is, etc.

    Returns:
        The current date and time as a formatted string (YYYY-MM-DD HH:MM:SS).
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
