# Professional Digital Twin

An AI-powered Digital Twin that represents my professional background, experience, skills, and career journey.

The application allows users to interact with an AI version of my professional profile through a conversational interface.

## Live Demo

**Try the Digital Twin:**  
https://huggingface.co/spaces/Sollie/twin

> 🚧 **Status: Active Development**
>
> This is my first independent Agentic AI application. The current version is deployed and functional, but I am continuing to improve its tool reliability, evaluation, scope control, and overall agent behavior.

---

## What It Does

The Digital Twin can:

- Answer questions about my professional background
- Use structured professional context to generate relevant responses
- Maintain conversation history
- Use OpenAI tool/function calling
- Execute external tools when appropriate
- Send notifications through Pushover
- Run an Agent Loop that allows the model to request tools and continue processing their results
- Provide a conversational interface through Gradio

---

## Architecture

```text
User
  │
  ▼
Gradio Interface
  │
  ▼
Digital Twin
  │
  ▼
OpenAI Model
  │
  ▼
Agent Loop
  │
  ├── Direct response
  │
  └── Tool call
        │
        ▼
    Python Tool
        │
        └── Pushover / External Action
```

The application is intentionally built without an agent framework so that I can understand the underlying mechanics of tool calling, context, and agent loops before moving to higher-level frameworks.

---

## Core Components

### `app.py`

The main application.

It:

- Initializes the OpenAI client
- Loads the Digital Twin system prompt
- Maintains conversation history
- Sends requests to the OpenAI model
- Detects tool calls
- Executes requested tools
- Returns tool results to the model
- Continues the Agent Loop until the model produces a final response
- Provides the Gradio chat interface

### `context.py`

Contains the Digital Twin's professional context and system instructions.

This gives the model the information it needs to respond as my professional Digital Twin.

### `tools.py`

Contains the tools available to the Digital Twin.

The tool system allows the model to request actions rather than only generating text.

One of the current integrations is Pushover for external notifications.

### `styles.py`

Contains the Gradio interface styling, JavaScript, and example prompts used by the application.

---

## Agent Loop

The Digital Twin uses a simple tool-calling Agent Loop:

```text
User message
      ↓
LLM
      ↓
Does the model need a tool?
      │
   ┌──┴──┐
   │     │
  No    Yes
   │     │
   │     ▼
   │   Execute tool
   │     │
   │     ▼
   │ Return tool result
   │     │
   └─────┘
      ↓
Final response
```

This allows the model to move beyond a single LLM response and interact with external functionality.

---

## Technologies

- Python
- OpenAI API
- Gradio
- Pushover
- Function / Tool Calling
- Conversation History
- Context Engineering
- Agent Loops
- Python Modules

---

## Deployment

The application is deployed as a public Gradio Space on Hugging Face.

**Live application:**

https://huggingface.co/spaces/Sollie/twin

The application uses environment variables for sensitive credentials rather than storing API keys in the repository.

### Required Secrets

```text
OPENAI_API_KEY
PUSHOVER_USER
PUSHOVER_TOKEN
```

These are configured in the deployment environment and are not committed to GitHub.

---

## Running Locally

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

Set the required environment variables and run:

```bash
python app.py
```

The application will launch through Gradio.

---

## Current Development

This project is actively evolving.

Current areas of improvement include:

- Improving tool reliability
- Debugging notification behavior
- Adding stronger scope control
- Evaluating agent responses
- Improving the Agent Loop
- Adding more useful tools
- Improving the Digital Twin's professional context
- Exploring memory and retrieval
- Experimenting with agent frameworks

---

## What I Learned

This project helped me move from learning individual Agentic AI concepts to combining them into a working application.

Key concepts implemented include:

- Context engineering
- LLM tool/function calling
- Conversation history
- Agent Loops
- Dynamic tool execution
- Modular Python applications
- External API integrations
- Gradio application development
- Environment-based secret management
- Cloud deployment

The project is part of my broader **Agentic AI Engineering** learning journey.
