#!/usr/bin/env python3

"""
Function that measure the runtime of a function that
waits for a given number of seconds
"""

from time import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of a function that waits for a given number of seconds.

    Args:
      n (int): The number of times to wait.
      max_delay (int): The maximum delay in seconds.

    Returns:
      float: The average runtime per wait.

    """
    start_time = time()
    wait_n(n, max_delay)
    end_time = time()

    total_time = end_time - start_time
    return total_time / n
