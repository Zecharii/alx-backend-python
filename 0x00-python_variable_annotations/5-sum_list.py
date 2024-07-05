#!/usr/bin/env python3
"""
Type-annotated function sum_list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculates the sum of all elements in a list of floats.

    Args:
        input_list: A list of floats.

    Returns:
        The sum of all elements in the list as a float.
    """

    return float(sum(input_list))
