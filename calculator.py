"""Simple command-line calculator."""

def main():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid number input.")
        return

    operation = input(
        "Choose an operation (add, subtract, multiply, divide): "
    ).strip().lower()

    if operation == "add":
        result = first + second
    elif operation == "subtract":
        result = first - second
    elif operation == "multiply":
        result = first * second
    elif operation == "divide":
        if second == 0:
            print("Error: Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Unknown operation.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
