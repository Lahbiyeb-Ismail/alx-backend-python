#!/usr/bin/env python3

"""
Asynchronous function that waits for a random amount
of time and returns the delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random amount
    of time and returns the delay.

    Args:
      max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
      float: The delay in seconds.

    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
