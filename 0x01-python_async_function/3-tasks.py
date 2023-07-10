#!/usr/bin/env python3
"""
task_wait-random file
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function that takes an integer max_delay and returns
    an asyncio.Task

    Args:
        max_delay (int): delay time

    Returns:
        asyncio.Task: return value
    """
    return asyncio.create_task(wait_random(max_delay))
