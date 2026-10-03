
import pytest

from agent import execute_tool


def test_execute_multiply():
    result = execute_tool(
        "calculator",
        {"a": 12, "b": 5, "operation": "multiply"},
    )
    assert result == 60


def test_execute_add():
    result = execute_tool(
        "calculator",
        {"a": 1000, "b": 36, "operation": "add"},
    )
    assert result == 1036


def test_unknown_tool():
    with pytest.raises(ValueError, match="Unknown tool"):
        execute_tool("unknown_tool", {})


def test_invalid_operation():
    with pytest.raises(ValueError, match="Unsupported"):
        execute_tool(
            "calculator",
            {"a": 2, "b": 3, "operation": "power"},
        )


def test_invalid_number():
    with pytest.raises(ValueError, match="must be numbers"):
        execute_tool(
            "calculator",
            {"a": "12", "b": 5, "operation": "multiply"},
        )


def test_boolean_is_not_a_number():
    with pytest.raises(ValueError, match="must be numbers"):
        execute_tool(
            "calculator",
            {"a": True, "b": 5, "operation": "multiply"},
        )