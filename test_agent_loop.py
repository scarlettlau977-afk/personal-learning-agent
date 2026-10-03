
from types import SimpleNamespace
from unittest.mock import Mock

from agent import run_agent


def test_agent_returns_final_answer():
    # Simulate a model response without tool calls.
    message = SimpleNamespace(
        content="Hello!",
        tool_calls=None,
        model_dump=lambda **kwargs: {
            "role": "assistant",
            "content": "Hello!",
        },
    )

    response = SimpleNamespace(
        choices=[
            SimpleNamespace(message=message)
        ]
    )

    client = Mock()
    client.chat.completions.create.return_value = response

    result = run_agent(
        client,
        "Say hello",
        max_steps=5,
    )

    assert result == "Hello!"
    client.chat.completions.create.assert_called_once()


def test_agent_executes_tool_and_returns_result():
    # First response: the model requests a calculator tool call.
    tool_call = SimpleNamespace(
        id="call_123",
        function=SimpleNamespace(
            name="calculator",
            arguments='{"a": 12, "b": 5, "operation": "multiply"}',
        ),
    )

    first_message = SimpleNamespace(
        content=None,
        tool_calls=[tool_call],
        model_dump=lambda **kwargs: {
            "role": "assistant",
            "tool_calls": [{"id": "call_123"}],
        },
    )

    # Second response: the model gives the final answer.
    final_message = SimpleNamespace(
        content="The answer is 60.",
        tool_calls=None,
        model_dump=lambda **kwargs: {
            "role": "assistant",
            "content": "The answer is 60.",
        },
    )

    responses = [
        SimpleNamespace(
            choices=[SimpleNamespace(message=first_message)]
        ),
        SimpleNamespace(
            choices=[SimpleNamespace(message=final_message)]
        ),
    ]

    client = Mock()
    client.chat.completions.create.side_effect = responses

    result = run_agent(
        client,
        "What is 12 multiplied by 5?",
        max_steps=5,
    )

    assert result == "The answer is 60."
    assert client.chat.completions.create.call_count == 2

    # Check that the tool result was returned to the model.
    second_call = client.chat.completions.create.call_args_list[1]
    messages = second_call.kwargs["messages"]

    tool_messages = [
        message for message in messages
        if message.get("role") == "tool"
    ]

    assert len(tool_messages) == 1
    assert tool_messages[0]["content"] == "60"
    assert tool_messages[0]["tool_call_id"] == "call_123"

def test_agent_stops_at_max_steps():
    # Simulate a model that keeps requesting a tool.
    tool_call = SimpleNamespace(
        id="call_repeat",
        function=SimpleNamespace(
            name="calculator",
            arguments='{"a": 1, "b": 1, "operation": "add"}',
        ),
    )

    message = SimpleNamespace(
        content=None,
        tool_calls=[tool_call],
        model_dump=lambda **kwargs: {
            "role": "assistant",
            "content": None,
            "tool_calls": [{"id": "call_repeat"}],
        },
    )

    response = SimpleNamespace(
        choices=[SimpleNamespace(message=message)]
    )

    client = Mock()
    client.chat.completions.create.return_value = response

    result = run_agent(
        client,
        "Keep calculating",
        max_steps=2,
    )

    assert result is None
    assert client.chat.completions.create.call_count == 2