
import pytest

from src.calculator import Calculator

class TestCalculator:
    # Test cases for Calculator class

    def setup_method(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        result = self.calc.add(2, 3)
        assert result == 5

    def test_add_negative_numbers(self):
        result = self.calc.add(-2, -3)
        assert result == -5

    def test_add_mixed_numbers(self):
        result = self.calc.add(5, -3)
        assert result == 2

    def test_subtract_positive_numbers(self):
        result = self.calc.subtract(5, 3)
        assert result == 2

    def test_subtract_negative_result(self):
        result = self.calc.subtract(3, 5)
        assert result == -2

    def test_multiply_positive_numbers(self):
        result = self.calc.multiply(3, 4)
        assert result == 12

    def test_multiply_by_zero(self):
        result = self.calc.multiply(5, 0)
        assert result == 0

    def test_divide_positive_numbers(self):
        result = self.calc.divide(10, 2)
        assert result == 5.0

    def test_divide_by_zero(self):
        # Test division by zero - should raise ValueError
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

    def test_divide_negative_numbers(self):
        result = self.calc.divide(-10, -2)
        assert result == 5.0

    def test_power_positive_base_positive_exponent(self):
        result = self.calc.power(2, 3)
        assert result == 8

    def test_power_base_zero(self):
        result = self.calc.power(0, 5)
        assert result == 0

    def test_power_exponent_zero(self):
        result = self.calc.power(5, 0)
        assert result == 1

    def test_factorial_positive_number(self):
        result = self.calc.factorial(5)
        assert result == 120

    def test_factorial_zero(self):
        result = self.calc.factorial(0)
        assert result == 1

    def test_factorial_one(self):
        result = self.calc.factorial(1)
        assert result == 1

    def test_factorial_negative_number(self):
        # Test factorial of negative number - should raise ValueError
        with pytest.raises(ValueError):
            self.calc.factorial(-1)

    def test_history_tracking(self):
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)

        history = self.calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history
        assert "3 * 4 = 12" in history

    def test_clear_history(self):
        self.calc.add(1, 2)
        self.calc.clear_history()

        history = self.calc.get_history()
        assert len(history) == 0

    def test_get_last_result_with_history(self):
        self.calc.add(5, 3)
        result = self.calc.get_last_result()
        assert result == 8

    def test_get_last_result_empty_history(self):
        result = self.calc.get_last_result()
        assert result is None

    def test_float_operations(self):
        result = self.calc.add(1.5, 2.5)
        assert result == 4.0

        result = self.calc.divide(7.5, 2.5)
        assert result == 3.0

    def test_power_with_float_exponent(self):
        # This test will fail due to the bug in power method
        result = self.calc.power(2, 2.0)
        assert result == 4  # This should work but might fail due to range() issue
