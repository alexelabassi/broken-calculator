# Simple calculator class with intentional bugs

from typing import Union

class Calculator:

    def __init__(self):
        self.history = []

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        # Bug: Should raise ValueError for division by zero
        if b == 0:
            return None  # This should be: raise ValueError("Cannot divide by zero")

        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        # Bug: Off-by-one error in loop
        result = 1
        for i in range(exponent):  # Should be: range(int(exponent))
            result *= base
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def factorial(self, n: int) -> int:
        # Bug: Missing edge case handling
        if n < 0:
            return None  # Should raise ValueError

        result = 1
        for i in range(1, n + 1):
            result *= i
        self.history.append(f"{n}! = {result}")
        return result

    def get_history(self) -> list:
        # Get calculator history
        return self.history

    def clear_history(self) -> None:
        # Clear calculator history
        self.history = []

    def get_last_result(self) -> Union[int, float, None]:
        # Get the last calculator result
        # Bug: Should handle empty history
        if not self.history:
            return None

        last_entry = self.history[-1]
        # Extract result from history entry
        if "=" in last_entry:
            result_str = last_entry.split("=")[-1].strip()
            try:
                if "." in result_str:
                    return float(result_str)
                else:
                    return int(result_str)
            except ValueError:
                return None
        return None
