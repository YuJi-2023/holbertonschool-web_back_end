#!/usr/bin/env python3
"""an asynchronous coroutine waits and return"""
import random
import asyncio


async def wait_random(max_delay=10):
    """input is int and wait for a random seconds delay then return"""
    max_delay = random.random()
    await asyncio.sleep(max_delay)
    return max_delay
