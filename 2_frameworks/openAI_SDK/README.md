# OpenAI Agents SDK

My first framework-focused stage in Agentic AI.

I started this section after building an Agent Loop without a framework. That gave me a practical understanding of LLM calls, tools, loops, memory and external actions before introducing the OpenAI Agents SDK.

## Learning files

### `01_agents_and_runner.ipynb`

Combines the useful learning from Labs 1–3.

It covers:

- Agents and `Runner`
- Agent Loops
- Tracing and observability
- Streaming
- Function tools
- Sessions and memory
- Orchestration by code
- Agents as tools
- Handoffs
- Structured Outputs
- Guardrails

The unrelated model-provider exploration from Lab 3 is intentionally left out because it was not central to my framework learning.

### `deep_research_learning.ipynb`

Documents the Deep Research Agent from Lab 4.

It explains:

- What the system does
- The role of each agent
- Structured outputs between agents
- Parallel search execution
- Python orchestration
- Tool-based delivery
- How the agents form one larger system

## Learning → implementation

These notebooks are the learning record.

The actual Deep Research application is developed separately under:

```text
3_agents/
└── deep-research-agent/
```

The project follows a modular structure where each component has a clear responsibility and a main entry point connects the system.
