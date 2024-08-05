#!/usr/bin/env python3

"""
Function that waits for a random delay multiple times
and returns the sorted delays
"""

import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n, max_delay):
    """
    Asynchronously waits for a random delay multiple
    times and returns the sorted delays.

    Args:
      n (int): The number of times to wait for a random delay.
      max_delay (int): The maximum delay in seconds.

    Returns:
      List[float]: A list of delays in seconds, sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
