#!/usr/bin/env python3
"""
Summing a list of floats with type annotations.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.

    :param input_list: list of floats
    :return: sum of the list as a float
    """
    return sum(input_list)
