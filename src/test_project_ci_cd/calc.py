"""Module with calculations."""

from typing import TypeVar

T = TypeVar("T", int, float)


def get_sum(a: T, b: T) -> T:
    """Sum."""
    return a + b
