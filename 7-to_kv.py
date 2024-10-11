#!/usr/bin/env python3
"""
Converting a string and int/float to a tuple with type annotations.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string, and the second is the square of the int/float.
    
    :param k: a string
    :param v: an integer or float
    :return: a tuple (k, v**2)
    """
    return (k, float(v ** 2))
