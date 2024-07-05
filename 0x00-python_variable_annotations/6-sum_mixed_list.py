#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list.
"""
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of all elements in a list of integers and floats.

    Args:
        mxd_lst: A list containing integers and floats.

    Returns:
        The sum of all elements in the list as a float.
    """

    return float(sum(mxd_lst))
