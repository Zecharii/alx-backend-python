#!/usr/env/bin/python3
"""Validate code on function zoom_array.
"""
from typing import Tuple


def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int, ...]:
    """Zooms in on a list of integers by repeating each element a specified number of times.

    Args:
        lst: The list of integers to zoom in on.
        factor: The number of times to repeat each element (default: 2).

    Returns:
        A tuple containing the zoomed-in elements.
    """

    zoomed_in: Tuple[int, ...] = tuple(item for item in lst for i in range(factor))
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)  # Now using an integer for factor
