#!/usr/bin/env python3

"""
Function that converts a key-value pair to a tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string `k` and a number `v` (which can be either an int or a float)
    and returns a tuple containing `k` and the square of `v` as a float.

    Args:
      k (str): The string key.
      v (Union[int, float]): The number value.

    Returns:
      Tuple[str, float]: A tuple containing `k` and the
      Zsquare of `v` as a float.
    """
    float_num: float = v * v

    return (k, float_num)
