"""Chainlit UI application for the AI Agent Explorer Learning Lab.

This module provides a chat interface with the ability to toggle between
Basic LLM mode (no tools) and Agent Mode (with tools and reasoning).
"""

import chainlit as cl
from chainlit.input_widget import Switch
from agent import basic_llm_chat, agent_chat


@cl.on_chat_start
async def start():
    """Initialize the chat session with default mode and set up sidebar."""
    # Initialize conversation history for Basic LLM mode
    cl.user_session.set("messages", [])
    cl.user_session.set("mode", "basic")  # Default to basic LLM mode
    
    # Set up sidebar toggle switch
    settings = await cl.ChatSettings(
        [
            Switch(
                id="agent_mode",
                label="Agent Mode",
                initial=False,
                tooltip="Toggle to switch between Basic LLM and Agent Mode",
                description="Enable Agent Mode to use tools (calculator, time checker)"
            )
        ]
    ).send()
    
    # Update mode based on toggle state
    if settings.get("agent_mode", False):
        cl.user_session.set("mode", "agent")
    else:
        cl.user_session.set("mode", "basic")
    
    # Welcome message
    await cl.Message(
        content="Welcome to AI Agent Explorer! Use the toggle in the sidebar to switch between Basic LLM and Agent Mode."
    ).send()


@cl.on_settings_update
async def on_settings_update(settings):
    """Handle sidebar toggle changes."""
    agent_mode = settings.get("agent_mode", False)
    if agent_mode:
        cl.user_session.set("mode", "agent")
        await cl.Message(content="Switched to Agent Mode").send()
    else:
        cl.user_session.set("mode", "basic")
        await cl.Message(content="Switched to Basic LLM mode").send()


@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages based on the current mode."""
    mode = cl.user_session.get("mode", "basic")
    user_content = message.content
    
    if mode == "basic":
        # Basic LLM Mode - maintain message history manually
        messages = cl.user_session.get("messages", [])
        
        # Add user message to history
        messages.append({"role": "user", "content": user_content})
        
        # Get response from basic LLM
        try:
            response_content = basic_llm_chat(messages)
            
            # Add assistant response to history
            messages.append({"role": "assistant", "content": response_content})
            cl.user_session.set("messages", messages)
            
            # Send response to UI
            await cl.Message(content=response_content).send()
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            await cl.Message(content=error_msg).send()
    
    elif mode == "agent":
        # Agent Mode - use agent with tools
        # Thinking steps are logged to terminal via print_message_payload in agent.py
        try:
            response_content = agent_chat(user_content)
            await cl.Message(content=response_content).send()
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            await cl.Message(content=error_msg).send()


@cl.on_stop
async def on_stop():
    """Handle when user stops the conversation."""
    await cl.Message(content="Conversation stopped.").send()




# @cl.on_chat_resume
# async def on_chat_resume(thread: cl.ThreadDict):
#     """Handle chat resume (if using thread persistence)."""
#     cl.user_session.set("messages", thread.get("steps", []))


#@cl.password_auth_callback
def auth_callback(username: str, password: str):
    """Optional: Add password authentication."""
    # For learning lab, we'll skip authentication
    # Return None to disable auth
    return None
