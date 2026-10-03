
from tools import calculator


def test_add():
    assert calculator(2, 3, "add") == 5


def test_subtract():
    assert calculator(8, 3, "subtract") == 5


def test_multiply():
    assert calculator(12, 5, "multiply") == 60


def test_divide():
    assert calculator(10, 2, "divide") == 5


def test_divide_by_zero():
    assert calculator(10, 0, "divide") == "Error: Cannot divide by zero"


def test_unsupported_operation():
    assert calculator(2, 3, "power") == "Error: Unsupported operation"