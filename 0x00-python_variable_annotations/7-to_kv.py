#!/usr/bin/env python3
"""Type-annotated function to_kv.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple with a string key and the square of a numeric value.

    Args:
        k: The string key for the tuple.
        v: The numeric value (int or float) whose square will be the second element.

    Returns:
        A tuple containing the key (str) and the square of the value (float).
    """

    return k, float(v ** 2)
