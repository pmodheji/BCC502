"""Part 2, Module 4: Create a calculator organized into functions."""
from calc_operations import add, subtract, multiply, divide

OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(a, operator, b):
    """Apply an operator to two numbers. Return None if it is not valid."""
    operation = OPERATIONS.get(operator)
    if operation is None:
        return None
    return operation(a, b)


def main():
    a = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ").strip()
    b = float(input("Second number: "))
    result = calculate(a, operator, b)
    if result is None:
        print("That calculation is not valid.")
    else:
        print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    main()
