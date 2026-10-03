
import re
from tools import calculator


def main():
    print("Hello, Agent!")
    print("Available tool: calculator")

    task = input("What do you want me to calculate? ")

    # Step 1: Identify the operation
    task_lower = task.lower()

    if "multiply" in task_lower:
        operation = "multiply"
    elif "divide" in task_lower:
        operation = "divide"
    elif "add" in task_lower:
        operation = "add"
    elif "subtract" in task_lower:
        operation = "subtract"
    else:
        print("Sorry, I don't understand this operation.")
        return

    # Step 2: Extract numbers from the input
    numbers = re.findall(r"-?\d+(?:\.\d+)?", task)

    if len(numbers) != 2:
        print("Please provide exactly two numbers.")
        return

    # Step 3: Convert strings to numbers
    a = float(numbers[0])
    b = float(numbers[1])

    # Step 4: Call the tool
    result = calculator(a, b, operation)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()