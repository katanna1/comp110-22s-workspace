"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730479768"


class Simpy:
    """Models the Numpy Function."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor to initializse the values of the Simpy object."""
        self.values = values
    
    def __str__(self) -> str:
        """A str representation of the values from the list[str]."""
        return f"Simpy({self.values})"

    def fill(self, values: float, y: int) -> None:
        """Fill Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < y:
            self.values.append(values)
            i = i + 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in attributes with a range of values."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next: float = start
            while next < stop:
                self.values.append(next)
                next = step + next

    def sum(self) -> float:
        """Compute and return the sum of all items i nthe values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for the addition operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i = i + 1
        return result
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for the power operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i = i + 1
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload that produces a mask based on the equality of each item."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if rhs == self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i = i + 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i = i + 1
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload that produces a mask based on the equality of each item."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i = i + 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i = i + 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        if isinstance(rhs, int):
            result: float = self.values[rhs]
            return result
        else:
            result1 = Simpy([])
            assert len(self.values) == len(rhs)
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    result1.values.append(self.values[i])
                i = i + 1
            return result1
