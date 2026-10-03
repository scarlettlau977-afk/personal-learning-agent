
from getpass import getpass
from openai import OpenAI

api_key = getpass("Enter your API Key: ")

client = OpenAI(
    api_key=api_key,
    base_url="https://modelflare.dev/v1",
)

try:
    response = client.chat.completions.create(
        model="gpt-6-luna",
        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: API connection successful"
            }
        ],
    )

    print("\nModel response:")
    print(response.choices[0].message.content)

except Exception as error:
    print("\nRequest failed.")
    print(f"Error type: {type(error).__name__}")
    print(f"Details: {error}")