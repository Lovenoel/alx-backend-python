#!/usr/bin/env python3
"""
Element length function with type annotations.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains an element from the input iterable
    and its length.
    
    :param lst: an iterable of sequences
    :return: list of tuples (element, length of element)
    """
    return [(i, len(i)) for i in lst]
