#!/usr/bin/env python3
"""
Create a function that multiplies a float by a multiplier with type annotations.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a multiplier.
    
    :param multiplier: a float multiplier
    :return: function that multiplies a float by the multiplier
    """
    return lambda x: x * multiplier
