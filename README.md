# AI Agent Explorer - Learning Lab

A minimal, transparent Python application designed to help learners understand the difference between a standard LLM and an Agent. This learning repository demonstrates how tools, reasoning loops, and "memory" work in AI systems.

## 🎯 Learning Objectives

After using this lab, learners will understand:

1. **The Stateless Nature of LLMs**: See how "memory" is just a list of text messages passed to the model
2. **Tools as Python Functions**: Learn that agent "tools" are simply Python functions with descriptive docstrings
3. **The ReAct Pattern**: Observe the Reason + Act loop in action through visual thinking steps
4. **API Standardization**: Understand that most AI APIs follow the OpenAI-compatible format

## 📋 Prerequisites

- Python 3.11 or higher
- `uv` package manager ([installation guide](https://github.com/astral-sh/uv))
- OpenRouter API key ([get one here](https://openrouter.ai/keys))

## 🚀 Setup

1. **Clone or download this repository**

2. **Install dependencies using `uv`:**
   ```bash
   uv sync
   ```

3. **Set up environment variables:**
   
   Create a `.env` file in the project directory with any text editor and add this line:
   ```
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```
   
   Replace `your_actual_api_key_here` with your actual OpenRouter API key from https://openrouter.ai/keys

4. **Run the application:**
   ```bash
   uv run chainlit run app.py
   ```

   **Note:** The first run may take a while as dependencies are downloaded and installed.
   
   The application will start and open in your browser automatically.

![Chat UI](Assets/chat_UI.jpg)

![Basic Mode Payload](Assets/Basic_mode_Payload.jpg)

## 🎮 Usage

### Two Modes

1. **Basic LLM Mode** (default):
   - Standard chat interface with no tool access
   - Maintains conversation history manually
   - Watch the terminal to see the full message payload before each API call

2. **Agent Mode**:
   - Agent has access to tools (Magic Calculator, Time Checker)
   - Uses reasoning to decide when to call tools
   - Thinking steps are logged to the terminal
   - Terminal shows the message payload for transparency

### Switching Modes

Use the toggle button in the settings to switch between modes.

![Settings Button](Assets/setting_button.jpg)

![Switch to Agent Mode](Assets/switch_to_agent_mode.jpg)

![Agent Thinking Steps](Assets/agent_thnking_steps.jpg)

### Example Queries

**In Basic LLM Mode:**
- "What is 15 * 23?" (The LLM will try to calculate but has no tools)
- "What time is it?" (The LLM will guess or say it doesn't know)

**In Agent Mode:**
- "What is 15 * 23?" (The agent will use the Magic Calculator tool)
- "What time is it?" (The agent will use the Time Checker tool)

## 🔍 Transparency Feature

This lab includes a **transparency logging** feature. Every time a request is sent to the model, the **full message payload** (the complete conversation history) is printed to the terminal. This demonstrates that:

- LLMs are stateless - they don't "remember" anything
- "Memory" is just a list of text messages passed with each request
- The model sees the entire conversation history as plain text

Watch your terminal while using the app to see this in action!

## 📁 Project Structure

```
.
├── app.py              # Chainlit UI with mode toggle
├── agent.py            # LLM and agent logic with transparency logging
├── tools.py            # Tool definitions (Magic Calculator, Time Checker)
├── pyproject.toml      # Project dependencies and configuration
├── .env                # Environment variables (create this file - see Setup)
├── CUSTOMIZATION.md    # Guide for adding tools and changing models
└── README.md           # This file
```

## 🔧 Customization

Want to add your own tools or change the LLM model? Check out the [CUSTOMIZATION.md](CUSTOMIZATION.md) guide for step-by-step instructions.

## 🛠️ Technical Stack

- **Package Manager**: `uv` for fast Python package management
- **Agent Framework**: `smolagents` (Hugging Face) - minimal, transparent agent implementation
- **UI Framework**: `chainlit` - modern chat interface
- **LLM Provider**: **OpenRouter** - unified API for multiple models
- **Model**: Uses OpenAI-compatible API via OpenRouter

## 🎓 For Educators

This repository is designed to be "bomb-proof" - meaning:

- No over-complicated libraries hiding the core concepts
- All logic is transparent and easy to understand
- Functional programming style where possible
- Clear separation of concerns (UI, agent logic, tools)
- Terminal logging shows exactly what's happening under the hood

Learners can read the code and understand:
- How message history is maintained
- How tools are defined and called
- How the agent decides when to use tools
- How the model API works

## 📝 Notes

- The terminal transparency logs are crucial for understanding how LLMs work
- Switching modes mid-conversation is allowed - try it to see the difference!
- Agent Mode resets conversation history (by design) to show the difference in behavior
- Basic LLM Mode maintains full conversation history to demonstrate "memory"

## 🤝 Contributing

This is a learning lab - feel free to extend it with additional tools or features that help you to learn!

## 📄 License

This project is designed for educational purposes.

---

**Made by Mohammed Balkhair**
