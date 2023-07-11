#!/usr/bin/env python3
"""
basic async syntax
"""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """
    an asynchronous coroutine that takes in an integer argument
    for a random delay between 0 and argument passed (included and float value)
    seconds and eventually returns it.

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: return value
    """
    i = random.randint(0, max_delay)
    start = time.perf_counter()
    await asyncio.sleep(i)
    end = time.perf_counter() - start
    return end
