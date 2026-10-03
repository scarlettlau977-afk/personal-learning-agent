
import json
from getpass import getpass
from openai import OpenAI

api_key = getpass("Enter your API Key: ")

client = OpenAI(
    api_key=api_key,
    base_url="https://modelflare.dev/v1",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform a basic mathematical calculation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number"
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number"
                    },
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "The mathematical operation"
                    }
                },
                "required": ["a", "b", "operation"],
                "additionalProperties": False
            }
        }
    }
]

try:
    response = client.chat.completions.create(
        model="gpt-6-luna",
        messages=[
            {
                "role": "user",
                "content": "Use the calculator tool to multiply 12 by 5."
            }
        ],
        tools=tools,
        tool_choice="auto",
    )

    message = response.choices[0].message

    print("\nFinish reason:", response.choices[0].finish_reason)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            print("Tool name:", tool_call.function.name)
            print("Arguments:", tool_call.function.arguments)
    else:
        print("No tool call returned.")
        print("Model response:", message.content)

except Exception as error:
    print("\nRequest failed.")
    print("Error type:", type(error).__name__)
    print("Details:", str(error))