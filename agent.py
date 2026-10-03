
import json
import os
from openai import OpenAI

from tools import calculator


MODEL = "gpt-6-luna"
BASE_URL = "https://modelflare.dev/v1"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Perform a basic mathematical calculation."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                    "operation": {
                        "type": "string",
                        "enum": [
                            "add",
                            "subtract",
                            "multiply",
                            "divide",
                        ],
                    },
                },
                "required": ["a", "b", "operation"],
                "additionalProperties": False,
            },
        },
    }
]


def execute_tool(tool_name, arguments):
    """Execute a tool requested by the model."""

    if tool_name != "calculator":
        raise ValueError(f"Unknown tool: {tool_name}")

    allowed_operations = {
        "add", "subtract", "multiply", "divide"
    }

    if arguments.get("operation") not in allowed_operations:
        raise ValueError("Unsupported calculator operation")

    a = arguments.get("a")
    b = arguments.get("b")

    if (
        isinstance(a, bool) or not isinstance(a, (int, float))
        or isinstance(b, bool) or not isinstance(b, (int, float))
    ):
        raise ValueError("Calculator arguments must be numbers")

    return calculator(a, b, arguments["operation"])



def run_agent(client, task, max_steps=5):
    """Run the agent loop until it produces a final answer."""

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. "
                "Use the calculator tool for mathematical calculations. "
                "After receiving the tool result, explain the result "
                "clearly to the user."
            ),
        },
        {"role": "user", "content": task},
    ]

    for step in range(max_steps):
        print(f"\nAgent step: {step + 1}")

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )

        message = response.choices[0].message
        messages.append(message.model_dump(exclude_none=True))

        if not message.tool_calls:
            print("\nAgent:", message.content)
            return message.content

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"Calling tool: {tool_name}")
            print(f"Arguments: {arguments}")

            try:
                result = execute_tool(tool_name, arguments)
            except (ValueError, TypeError) as error:
                result = f"Tool execution failed: {error}"

            print(f"Tool result: {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result),
                }
            )

    print("\nAgent stopped: maximum number of steps reached.")
    return None


def main():
    api_key = os.getenv("MODELFLARE_API_KEY")

    if not api_key:
        raise ValueError(
            "Please set the MODELFLARE_API_KEY environment variable."
        )

    client = OpenAI(
        api_key=api_key,
        base_url=BASE_URL,
    )

    task = input("What do you want your agent to do? ")

    run_agent(client, task, max_steps=5)


if __name__ == "__main__":
    main()