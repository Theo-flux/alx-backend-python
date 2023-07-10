#!/usr/bin/env python3
"""
running coroutines concurrently
"""
from typing import List
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time with async

    Args:
        n (int): the number of times the coroutine should be run
        max_delay (int): the specified maximum delay for each instance of
        coroutine

    Returns:
        List[float]: list of delays from the concurrency
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
