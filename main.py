#!/usr/bin/env python3
"""CLI version of AI Agent Explorer - Learning Lab.

Run with: python main.py
"""

import os
import json
import sys
from dotenv import load_dotenv
from datetime import datetime
import math
import urllib.request

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    print("ERROR: OPENROUTER_API_KEY not found in environment.")
    sys.exit(1)

API_BASE = "https://openrouter.ai/api/v1"
MODEL = "openai/gpt-4o"



# Tools
def magic_calculator(expression):
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names.update({"abs": abs, "round": round, "min": min, "max": max})
    return str(eval(expression, {"__builtins__": {}}, allowed_names))

def time_checker():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "magic_calculator",
            "description": "Evaluate mathematical expressions safely.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "A mathematical expression"}
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "time_checker",
            "description": "Get the current date and time.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    }
]

# API Call
def make_api_call(messages, tools=None):
    payload = {"model": MODEL, "messages": messages}
    if tools:
        payload["tools"] = tools
        payload["tool_choice"] = "auto"
    
    print("\n--- API Request ---")
    print(json.dumps(payload, indent=2))
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        f"{API_BASE}/chat/completions",
        data=data,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        method='POST'
    )
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("\n--- API Response ---")
    print(json.dumps(result, indent=2))
    print()
    
    return result

# Basic LLM Mode
def basic_llm_chat(messages):
    response = make_api_call(messages)
    return response["choices"][0]["message"]["content"]

# Agent Mode
def agent_chat(user_message):
    messages = [{"role": "user", "content": user_message}]
    
    for _ in range(5):
        response = make_api_call(messages, tools=TOOLS)
        message = response["choices"][0]["message"]
        
        if "tool_calls" in message and message["tool_calls"]:
            messages.append(message)
            
            for tool_call in message["tool_calls"]:
                function_name = tool_call["function"]["name"]
                arguments = json.loads(tool_call["function"]["arguments"])
                
                print(f"Tool: {function_name}({arguments})")
                
                if function_name == "magic_calculator":
                    result = magic_calculator(arguments["expression"])
                elif function_name == "time_checker":
                    result = time_checker()
                
                print(f"Result: {result}\n")
                
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "name": function_name,
                    "content": result
                })
        else:
            return message["content"]
    
    return "Error: Maximum iterations reached"

# CLI
def main():
    print("AI Agent Explorer - CLI")
    print("Commands: 'basic' or '1', 'agent' or '2', 'quit'\n")
    
    mode = "basic"
    messages = []
    
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        
        if user_input.lower() in ["quit", "exit", "q"]:
            break
        
        if user_input.lower() in ["basic", "1"]:
            mode = "basic"
            messages = []
            continue
        
        if user_input.lower() in ["agent", "2"]:
            mode = "agent"
            messages = []
            continue
        
        if mode == "basic":
            messages.append({"role": "user", "content": user_input})
            response = basic_llm_chat(messages)
            messages.append({"role": "assistant", "content": response})
            print(f"Assistant: {response}\n")
        else:
            response = agent_chat(user_input)
            print(f"Assistant: {response}\n")

if __name__ == "__main__":
    main()
