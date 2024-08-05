#!/usr/bin/env python3

"""
Function that waits for `n` random delays and returns them in sorted order
"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for `n` random delays and returns them in sorted order.

    Args:
      n (int): The number of delays to wait for.
      max_delay (int): The maximum delay value in seconds.

    Returns:
      List[float]: A list of `n` random delays in seconds,
      sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
