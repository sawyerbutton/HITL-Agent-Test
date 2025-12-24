import argparse
from calculator import Calculator


def main():
    """A simple command-line calculator.

    Takes two numbers and an operator as input, performs the calculation,
    and prints the result.
    """
    parser = argparse.ArgumentParser(description="A simple command-line calculator.")
    parser.add_argument("num1", type=float, help="The first number.")
    parser.add_argument("operator", type=str, choices=["+", "-", "*", "/"], help="The operation to perform (+, -, *, /).")
    parser.add_argument("num2", type=float, help="The second number.")

    args = parser.parse_args()

    calculator = Calculator()

    try:
        if args.operator == "+":
            result = calculator.add(args.num1, args.num2)
        elif args.operator == "-":
            result = calculator.subtract(args.num1, args.num2)
        elif args.operator == "*":
            result = calculator.multiply(args.num1, args.num2)
        elif args.operator == "/":
            result = calculator.divide(args.num1, args.num2)
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()