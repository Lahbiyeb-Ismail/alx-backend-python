#!/usr/bin/env python3

"""
Async function that performs comprehension on an async generator.
"""

import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
    Async function that performs comprehension on an async generator.

    Returns:
      A list of values generated by the async generator.
    """
    return [generator async for generator in async_generator()]
