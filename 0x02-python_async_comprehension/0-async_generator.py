#!/usr/bin/env python3

"""
Asynchronous generator that yields random numbers between 0 and 10.
"""

import asyncio
import random
from typing import Any, Generator


async def async_generator() -> Generator[float, Any, None]:  # type: ignore
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
