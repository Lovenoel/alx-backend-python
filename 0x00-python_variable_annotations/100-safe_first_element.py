#!/usr/bin/env python3
"""
Safe first element function with type annotations.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence, if present. Otherwise,
    returns None.

    :param lst: a sequence (like a list or tuple) containing elements
    of any type
    :return: the first element of the sequence or None if the
    sequence is empty
    """
    if lst:
        return lst[0]
    else:
        return None
