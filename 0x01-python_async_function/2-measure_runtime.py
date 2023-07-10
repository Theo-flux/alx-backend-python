#!/usr/bin/env python3
"""
measure runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    function with integers n and max_delay as arguments that
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n (int): number of times to run wait_n
        max_delay (int): delay time

    Returns:
        float: time returned
    """
    start = time.perf_counter()
    await asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start

    return end/n
