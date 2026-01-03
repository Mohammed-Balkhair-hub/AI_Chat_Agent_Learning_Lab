"""Agent and LLM logic for the AI Agent Explorer Learning Lab.

This module demonstrates the difference between a basic LLM (stateless)
and an Agent (with tools and reasoning). It includes transparency logging
to show that "memory" is just a list of text messages.
"""

import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from smolagents import OpenAIModel, ToolCallingAgent
from tools import magic_calculator, time_checker

# Load environment variables
load_dotenv()


def get_model() -> OpenAIModel:
    """Initialize and return the OpenRouter model.
    
    Returns:
        OpenAIModel instance configured to use OpenRouter API.
    
    Raises:
        ValueError: If OPENROUTER_API_KEY is not found in environment.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found in environment. Please set it in .env file."
        )
    
    return OpenAIModel(
        model_id="openai/gpt-4o",  # Choose a model from https://openrouter.ai/models
        api_base="https://openrouter.ai/api/v1",
        api_key=api_key,
    )


def print_message_payload(messages: List[Dict[str, Any]], mode: str = "LLM"):
    """Print the full message payload to terminal for transparency.
    
    This demonstrates that "memory" is just text concatenation - the model
    receives the entire conversation history as a list of messages.
    
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
        mode: Mode identifier (LLM or Agent) for clarity in output
    """
    print("\n" + "=" * 80)
    print(f"TRANSPARENCY LOG: {mode} Mode - Full Message Payload")
    print("=" * 80)
    for i, msg in enumerate(messages, 1):
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        print(f"\n[{i}] Role: {role}")
        print(f"    Content: {content}")
    print("=" * 80 + "\n")


def basic_llm_chat(messages: List[Dict[str, Any]]) -> str:
    """Basic LLM chat function without tools.
    
    This is a stateless function that takes a message history and returns
    a response. The model has no access to tools - it can only generate text.
    
    Args:
        messages: List of message dictionaries in OpenAI format
                 (e.g., [{"role": "user", "content": "Hello"}])
    
    Returns:
        The model's response as a string.
    """
    model = get_model()
    
    # TRANSPARENCY: Print the full message payload before API call
    print_message_payload(messages, mode="Basic LLM")
    
    # OpenAIModel.generate can work with messages list directly
    # If not, we'll format it as a string conversation
    try:
        # Try passing messages directly (OpenAI format)
        response = model.generate(messages)
    except TypeError:
        # Fallback: format messages as a conversation string
        conversation = "\n".join(
            [f"{msg['role']}: {msg['content']}" for msg in messages]
        )
        response = model.generate(conversation)
    
    # Extract content if response is a ChatMessage object, otherwise use as string
    if hasattr(response, 'content'):
        return str(response.content)
    return str(response)


def agent_chat(user_message: str) -> str:
    """Agent chat function with tools and reasoning.
    
    This function creates an agent with access to tools. The agent can
    reason about when to use tools and can call them during conversation.
    
    Args:
        user_message: The user's message as a string.
    
    Returns:
        The agent's response as a string.
    """
    model = get_model()
    
    # Create agent with tools (ToolCallingAgent for simple tool use, not code execution)
    tools = [magic_calculator, time_checker]
    agent = ToolCallingAgent(tools=tools, model=model)
    
    # For transparency, we need to show the messages the agent will use
    # The agent internally manages message history, but we can still log the user input
    print_message_payload(
        [{"role": "user", "content": user_message}],
        mode="Agent"
    )
    
    # Run the agent - it will handle tool calling and reasoning internally
    response = agent.run(user_message)
    
    # Extract content if response is a ChatMessage object, otherwise use as string
    if hasattr(response, 'content'):
        return str(response.content)
    return str(response)
