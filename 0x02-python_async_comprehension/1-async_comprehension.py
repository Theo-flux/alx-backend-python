#!/usr/bin/env python3
"""
async comprehension file
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async comprehension

    Returns:
        List[float]: returned value
    """
    return [gen async for gen in async_generator()]
