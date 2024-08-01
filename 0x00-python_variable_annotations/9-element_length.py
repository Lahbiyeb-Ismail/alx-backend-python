#!/usr/bin/env python3

"""
Function that calculate the length of each element in the given list.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the given list.

    Args:
      lst (Iterable[Sequence]): The list of elements.

    Returns:
      List[Tuple[Sequence, int]]: A list of tuples,
      where each tuple contains an element from the input
      list and its corresponding length.

    """
    return [(i, len(i)) for i in lst]
