#!/usr/bin/env python3
"""
measure runtime file
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures total time to run four parallel coroutines

    Returns:
        float: return time
    """
    start = time.perf_counter()
    await asyncio.gather(
        *tuple(
            asyncio.create_task(async_comprehension())
            for _ in range(4)
        ))
    end = time.perf_counter() - start

    return end
