#!/usr/bin/env python3


"""
Function that returns the first element of a sequence
if it is not empty, otherwise returns None
"""

from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it is not
    empty, otherwise returns None.

    Args:
      lst (Sequence[Any]): The sequence from which to
      retrieve the first element.

    Returns:
      Union[Any, NoneType]: The first element of the
      sequence if it is not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
