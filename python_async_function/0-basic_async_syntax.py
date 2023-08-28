#!/usr/bin/env python3
"""an asynchronous coroutine waits and return"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """input is int and wait for a random seconds delay then return"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
