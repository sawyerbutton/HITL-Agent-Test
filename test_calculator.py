import pytest
from calculator import Calculator


class TestCalculator:
    def setup_class(self):
        self.calculator = Calculator()

    def test_add(self):
        assert self.calculator.add(1, 2) == 3
        assert self.calculator.add(-1, 1) == 0
        assert self.calculator.add(-1, -1) == -2
        assert self.calculator.add(0, 0) == 0
        assert self.calculator.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        assert self.calculator.subtract(2, 1) == 1
        assert self.calculator.subtract(1, 2) == -1
        assert self.calculator.subtract(-1, -1) == 0
        assert self.calculator.subtract(0, 0) == 0
        assert self.calculator.subtract(3.5, 1.5) == 2.0

    def test_multiply(self):
        assert self.calculator.multiply(2, 3) == 6
        assert self.calculator.multiply(-1, 2) == -2
        assert self.calculator.multiply(-1, -1) == 1
        assert self.calculator.multiply(0, 5) == 0
        assert self.calculator.multiply(2.5, 2) == 5.0

    def test_divide(self):
        assert self.calculator.divide(6, 3) == 2
        assert self.calculator.divide(-4, 2) == -2
        assert self.calculator.divide(5, 2) == 2.5
        assert self.calculator.divide(0, 5) == 0
        assert self.calculator.divide(7.5, 2.5) == 3.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError) as e:
            self.calculator.divide(1, 0)
        assert str(e.value) == "Cannot divide by zero."