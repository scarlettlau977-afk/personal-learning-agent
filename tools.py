def calculator(a, b, operation):
    """Perform a basic mathematical calculation."""

    if operation == "add":
            return a + b

    elif operation == "subtract":
            return a - b

    elif operation == "multiply":
            return a * b

    elif operation == "divide":
           if  b == 0:
                 return"Error: Cannot divide by zero"
           return a / b
    else:
           return "Error: Unsupported operation"