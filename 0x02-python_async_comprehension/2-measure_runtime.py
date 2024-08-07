#!/usr/bin/env python3

"""
Measures the runtime of the async_comprehension function.
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the async_comprehension function.

    Returns:
      float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
