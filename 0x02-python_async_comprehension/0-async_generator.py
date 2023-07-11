#!/usr/bin/env python3
"""
async generator function
"""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
