class Calculator:
    """A simple calculator class.

    Provides methods for basic arithmetic operations: add, subtract, multiply, and divide.
    """

    def add(self, x, y):
        """Adds two numbers.

        Args:
            x: The first number.
            y: The second number.

        Returns:
            The sum of x and y.
        """
        return x + y

    def subtract(self, x, y):
        """Subtracts two numbers.

        Args:
            x: The first number.
            y: The second number.

        Returns:
            The difference of x and y.
        """
        return x - y

    def multiply(self, x, y):
        """Multiplies two numbers.

        Args:
            x: The first number.
            y: The second number.

        Returns:
            The product of x and y.
        """
        return x * y

    def divide(self, x, y):
        """Divides two numbers.

        Args:
            x: The first number.
            y: The second number.

        Returns:
            The quotient of x and y.

        Raises:
            ValueError: If y is zero.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y