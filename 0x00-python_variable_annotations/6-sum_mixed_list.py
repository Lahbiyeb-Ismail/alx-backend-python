#!/usr/bin/env python3

"""
Function that calculate the sum of a mixed list of integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
      mxd_lst (Union[int, float]): The mixed list of integers and floats.

    Returns:
      float: The sum of the elements in the mixed list.
    """
    sum: float = 0

    for num in mxd_lst:
        sum += num

    return sum
