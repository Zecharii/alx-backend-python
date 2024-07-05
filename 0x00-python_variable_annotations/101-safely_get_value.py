#!/usr/env/bin/python3
"""Type-annotation to function.
"""
from typing import TypeVar, Union

T = TypeVar('T')  # Define a type variable to represent the type of the value in the dictionary


def safely_get_value(dct: dict[str, T], key: str, default: Union[T, NoneType] = None) -> Union[T, NoneType]:
    """Gets a value from a dictionary with a default value if the key is not found.

    Args:
        dct: The dictionary to get the value from.
        key: The key of the value to retrieve.
        default: The default value to return if the key is not found (optional).

    Returns:
        The value associated with the key or the default value if the key is not found.
    """

    if key in dct:
        return dct[key]
    else:
        return default
