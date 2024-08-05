#!/usr/bin/env python3

"""
Function that creates and returns an asyncio.Task
object that wraps the wait_random function
"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task object that
    wraps the wait_random function.

    Args:
      max_delay (int): The maximum delay value for wait_random function.

    Returns:
      asyncio.Task: An asyncio.Task object that represents
      the wrapped wait_random function.
    """
    return asyncio.Task(wait_random(max_delay))
