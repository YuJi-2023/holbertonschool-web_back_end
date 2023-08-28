#!/usr/bin/env python3
"""an asynchronous coroutine wait_n"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes int max_delay and return an asyncio.Task"""
    async def task():
        result = await wait_random(max_delay)
        return result

    return asyncio.create_task(task())
