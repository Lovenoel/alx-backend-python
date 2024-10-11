#!/usr/bin/env python3
"""
Summing a mixed list of integers and floats with type annotations.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list of integers and floats.
    
    :param mxd_lst: list containing integers and floats
    :return: sum of the list as a float
    """
    return sum(mxd_lst)
