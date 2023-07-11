#!/usr/bin/env python3
"""
running coroutines concurrently
"""
from typing import List
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time with async

    Args:
        n (int): the number of times the coroutine should be run
        max_delay (int): the specified maximum delay for each instance of
        coroutine

    Returns:
        List[float]: list of delays from the concurrency
    """
    i = random.randint(0, max_delay)
    time_list: List[float] = await asyncio.gather(
        *tuple(asyncio.create_task(wait_random(max_delay) )for i in range(n))
    )

    return sorted(time_list)
