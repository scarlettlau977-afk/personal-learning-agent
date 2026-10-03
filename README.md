

\# scarlett's-agent-demo



A lightweight, testable tool-calling agent built with Python and the OpenAI-compatible API.



The project explores the fundamentals of agent orchestration, including model interaction, tool execution, input validation, multi-step reasoning workflows, and automated testing. It is designed to evolve into an experimental framework for evaluating agent memory systems.



## Current Status



- \[x] LLM API integration

- \[x] Function tool calling

- \[x] Calculator tool execution

- \[x] Tool argument validation

- \[x] Multi-step agent loop

- \[x] Maximum execution-step limit

- \[x] Automated unit and orchestration tests

- \[ ] Persistent memory storage

- \[ ] Memory retrieval and update strategies

- \[ ] Agent memory evaluation benchmarks



## Features



### 1. Tool Calling



The model can request a calculator tool to perform basic arithmetic operations:



- Addition

- Subtraction

- Multiplication

- Division



### 2. Input Validation



The agent validates tool names, supported operations, and numeric arguments before executing a tool. Boolean values are rejected as numeric inputs.



### 3. Multi-Step Orchestration



The agent maintains conversation history, executes requested tools, and returns tool results to the model for further processing.



### 4. Execution Limit



A configurable maximum number of model steps prevents the agent loop from running indefinitely.



### 5. Automated Testing



Mock model responses are used to test agent orchestration without making live API requests.



## Architecture



```mermaid

flowchart TD

&#x20;   A\[User Task] --> B\[Agent]

&#x20;   B --> C\[LLM API]

&#x20;   C --> D{Tool Call Requested?}

&#x20;   D -- No --> E\[Final Answer]

&#x20;   D -- Yes --> F\[Validate Tool Arguments]

&#x20;   F --> G\[Execute Calculator]

&#x20;   G --> H\[Append Tool Result]

&#x20;   H --> B

```



## Project Structure



```text

personal-learning-agent/

├── agent.py              # Agent orchestration and tool execution

├── tools.py              # Calculator implementation

├── model_api_demo.py     # Standalone model API example

├── tool\_call\_demo.py     # Standalone tool-calling example

├── test\_tools.py         # Calculator unit tests

├── test\_agent.py         # Tool execution and validation tests

├── test\_agent\_loop.py    # Agent orchestration tests

├── .gitignore            # Excludes local and generated files

└── README.md             # Project documentation

```



## Requirements



- Python 3.13 (the development environment used for this project)

- An API key for a compatible model provider

- The `openai` Python SDK

- `pytest` for running tests



## Installation



### 1. Clone the repository



```bash

git clone https://github.com/scarlettlau977-afk/scarlett-s-agent-demo

cd scarlett-s-agent-demo

```



Replace the placeholder with the actual repository URL after publishing the project.



### 2. Create and activate a virtual environment



Windows CMD:



```cmd

python -m venv .venv

.venv\\Scripts\\activate

```



### 3. Install dependencies



```cmd

python -m pip install openai pytest

```



## Configuration



The agent reads its API key from the `MODELFLARE_API_KEY` environment variable.



Windows CMD:



```cmd

set MODELFLARE_API_KEY=YOUR\_API\_KEY

```



Replace `YOUR\_API\_KEY` locally with your own key. Do not commit API keys or share them in source files.



The current implementation uses the following model configuration in `agent.py`:



- Base URL: `https://modelflare.dev/v1`

- Model ID: `gpt-6-luna`



These values may need to be changed to match the model provider and model available to you.



## Usage



Run the agent from the project root:



```cmd

python agent.py

```



Enter a task when prompted. For example:



```text

What do you want your agent to do? What is 12 multiplied by 5?

```



The agent may request the calculator tool, execute the calculation, and use the result to produce a final answer.



A valid API key and access to the configured model are required for live requests.



## Testing



Run the full test suite:



```cmd

python -m pytest -v

```



The current development version has **15 passing tests**.



The tests cover:



- Calculator arithmetic and error cases

- Tool name and argument validation

- Direct final-answer handling

- Tool execution and result handoff

- Maximum-step termination



The orchestration tests use mocked model responses, so they do not require live model API calls.



## Current Limitations



- The agent supports a basic calculator tool rather than a broad tool ecosystem.

- Conversation history exists only during the current run.

- There is no persistent memory, retrieval layer, or memory evaluation benchmark yet.

- The configured model endpoint and model ID depend on provider availability.

- The maximum-step limit does not replace request timeouts, retry policies, or cost controls.



## Roadmap



### Phase 1: Agent Reliability

- \[x] Separate agent orchestration from application entry-point logic

- \[x] Validate tool arguments

- \[x] Add automated orchestration tests



### Phase 2: Memory System

- \[ ] Define a memory data model

- \[ ] Implement memory storage and retrieval

- \[ ] Support memory updates and deletion

- \[ ] Test memory persistence across runs



### Phase 3: Memory Evaluation

- \[ ] Build a reproducible evaluation dataset

- \[ ] Compare an agent with and without memory

- \[ ] Measure retrieval accuracy and task success

- \[ ] Record failures and produce experiment reports



## Learning Goals



This project is intended to explore:



- LLM tool-calling workflows

- Agent control flow and orchestration

- Defensive input validation

- Unit testing and mocking

- Reproducible evaluation of agent memory systems



## License



No license has been added yet. Reuse and redistribution permissions have not been specified.

