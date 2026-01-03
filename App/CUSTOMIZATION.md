# Customization Guide

This guide explains how to customize the **UI version** of AI Agent Explorer (in the `App/` folder) by adding new tools or changing the LLM model.

## 🛠️ Adding a New Tool

Tools are simple Python functions decorated with `@tool`. Here's how to add your own:

### Step 1: Open `App/tools.py`

All tools are defined in the `App/tools.py` file.

### Step 2: Add Your Tool Function

Add your tool function anywhere in the file (after the imports, before or after existing tools). Follow this pattern:

```python
@tool
def your_tool_name(parameter: type) -> str:
    """Brief description of what the tool does.

    This is the detailed description that the LLM will see.
    Make it clear and specific so the agent knows when to use it.

    Args:
        parameter: Description of the parameter

    Returns:
        Description of what the tool returns
    """
    # Your tool logic here
    result = "your result"
    return str(result)
```

### Step 3: Import Your Tool in `App/agent.py`

Open `App/agent.py` and find line 12 (the imports section):

```python
from tools import magic_calculator, time_checker
```

Add your new tool to the import list:

```python
from tools import magic_calculator, time_checker, your_tool_name
```

### Step 4: Add Tool to Agent

Find line 112 in `agent.py`:

```python
tools = [magic_calculator, time_checker]
```

Add your tool to the list:

```python
tools = [magic_calculator, time_checker, your_tool_name]
```

### Example: Adding a Weather Tool

Here's a complete example:

**In `App/tools.py` (add after line 54):**
```python
@tool
def weather_checker(city: str) -> str:
    """Get the current weather for a city.

    This tool retrieves weather information for a specified city.
    Useful when users ask about weather conditions.

    Args:
        city: The name of the city (e.g., "New York", "London")

    Returns:
        A string describing the current weather in the city.
    """
    # In a real implementation, you'd call a weather API here
    return f"The weather in {city} is sunny, 72°F"
```

**In `App/agent.py` line 12:**
```python
from tools import magic_calculator, time_checker, weather_checker
```

**In `App/agent.py` line 112:**
```python
tools = [magic_calculator, time_checker, weather_checker]
```

That's it! Your new tool is now available in Agent Mode.

---

## 🤖 Changing the LLM Model

The LLM model is configured in the `get_model()` function in `App/agent.py`.

### Step 1: Open `App/agent.py`

### Step 2: Find the Model Configuration

Locate the `get_model()` function starting at **line 18**. Find line 34:

```python
model_id="openai/gpt-4o",
```

### Step 3: Change the Model

Replace `"openai/gpt-4o"` with any model from [OpenRouter's model list](https://openrouter.ai/models).

**Popular options:**
- `"openai/gpt-4o-mini"` - Faster and cheaper
- `"openai/gpt-4o"` - More capable (current default)
- `"anthropic/claude-3.5-sonnet"` - Claude model
- `"google/gemini-pro-1.5"` - Google's model
- `"meta-llama/llama-3.1-70b-instruct"` - Open source option

**Example change (line 34):**
```python
model_id="openai/gpt-4o-mini",  # Changed to a faster, cheaper model
```

### Step 4: Optional - Adjust API Base (if needed)

The API base is already configured correctly for OpenRouter at **line 35**:
```python
api_base="https://openrouter.ai/api/v1",
```

You typically don't need to change this unless you're using a different API provider.

### Complete Example

Here's what the `get_model()` function looks like with a different model:

```python
def get_model() -> OpenAIModel:
    """Initialize and return the OpenRouter model."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found in environment. Please set it in .env file."
        )
    
    return OpenAIModel(
        model_id="openai/gpt-4o-mini",  # Changed model here
        api_base="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
```

---

## 📝 Summary

**To add a tool:**
1. Add function in `App/tools.py` with `@tool` decorator
2. Import it in `App/agent.py` line 12
3. Add it to the tools list in `App/agent.py` line 112

**To change the model:**
1. Edit `model_id` in `App/agent.py` line 34

That's all you need to customize the AI Agent Explorer!
