#!/usr/bin/env python3
"""
async generator function
"""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async generator function to generate 10 random numbers

    Returns:
        AsyncGenerator[float, None]: return value is none

    Yields:
        Iterator[AsyncGenerator[float, None]]: float
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
