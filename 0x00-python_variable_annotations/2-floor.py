#!/usr/bin/env python3
"""
Type-annotated function floor.
"""


import math


def floor(n: float) -> int:
    """Returns the floor of a float number.

    The floor of a number is the largest integer less than or equal to the number.

    Args:
        n: The float number to find the floor of.

    Returns:
        The floor of n as an integer.
    """

    return math.floor(n)
