#!/usr/bin/env python3
"""create a coroutine async_generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """the coroutine loop 10 times and wait 1 sec, then random out a number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
