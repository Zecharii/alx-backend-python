#!/usr/env/bin/python3
"""Type-annotated function make_multiplier.
"""
from typing import Callable, float


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a new function that multiplies a float by a given multiplier.

    Args:
        multiplier: The float value to use as the multiplier.

    Returns:
        A new function that takes a float as input and returns its product with the multiplier.
    """

    def inner(number: float) -> float:
        """Multiplies a float by the multiplier."""
        return number * multiplier

    return inner
