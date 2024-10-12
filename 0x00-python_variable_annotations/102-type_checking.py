#!/usr/bin/env python3
"""
Zoom array function with type annotations.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Repeats each element in the input tuple according to the zoom
    factor.

    :param lst: a tuple of integers
    :param factor: the zoom factor to repeat each element
    (default is 2)
    :return: a list of integers with each element repeated 'factor'
    times
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
