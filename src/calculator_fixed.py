from typing import Union, List, Optional

class Calculator:
    def __init__(self):
        self.history = []
        self.last_result = None

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result

    def power(self, base: float, exponent: float) -> float:
        result = base ** exponent
        self._add_to_history(f"{base} ** {exponent} = {result}")
        return result

    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("Cannot compute factorial of a negative number")
        result = 1
        for i in range(2, n + 1):
            result *= i
        self._add_to_history(f"factorial({n}) = {result}")
        return result

    def get_history(self) -> list:
        return self.history

    def clear_history(self) -> None:
        self.history.clear()
        self.last_result = None

    def get_last_result(self) -> float:
        return self.last_result

    def _add_to_history(self, entry: str) -> None:
        self.history.append(entry)
        self.last_result = float(entry.split('=')[-1].strip())
