#!/usr/bin/env python3

"""
Zooms in on the given list by repeating each element a certain number of times
"""

from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the given list by repeating each
    element a certain number of times.

    Args:
      lst (Tuple): The input list to be zoomed in.
      factor (int, optional): The number of times
      each element should be repeated. Defaults to 2.

    Returns:
      List: The zoomed-in list.

    """
    zoomed_in: List[Any] = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
zoom_3x = zoom_array(array, 3)
zoom_3x = zoom_array(array, 3)
