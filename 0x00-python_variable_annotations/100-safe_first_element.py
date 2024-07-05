#!/usr/env/bin/python3
"""Duck-type annotation of function.
"""
def safe_first_element(lst: typing.Sequence) -> typing.Union[typing.Any, NoneType]:
    """Returns the first element of a sequence if it exists, otherwise None.

    Args:
        lst: A sequence of any type.

    Returns:
        The first element of the sequence or None if the sequence is empty.
    """

    if lst:
        return lst[0]
    else:
        return None
