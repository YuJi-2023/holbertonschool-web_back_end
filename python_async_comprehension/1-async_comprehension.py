#!/usr/bin/env python3
"""create a coroutine async_comprehension that takes no arguments"""
import random
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """the coroutine collect 10 random numbers using async comprehension over\
        async_generator and then return the list of numbers"""
    dataset = [data async for data in async_generator()]
    return dataset
