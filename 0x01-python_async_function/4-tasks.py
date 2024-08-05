#!/usr/bin/env python3

"""
Function that waits for a random delay multiple times
and returns the sorted delays
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a random delay multiple
    times and returns the sorted delays.

    Args:
      n (int): The number of times to wait for a random delay.
      max_delay (int): The maximum delay in seconds.

    Returns:
      List[float]: A list of delays in seconds, sorted in ascending order.
    """

    de = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))

    for i in range(1, len(de)):
        key = de[i]
        j = i - 1
        while j >= 0 and key < de[j]:
            de[j + 1] = de[j]
            j -= 1
        de[j + 1] = key

    return de
