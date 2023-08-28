#!/usr/bin/env python3
"""an asynchronous coroutine wait_n"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes two ints and return the list of all delays ascendingly"""
    result_list = []
    for count in range(n):
        delay = await wait_random(max_delay)
        result_list.append(delay)
    sorted_list = sorted(result_list)
    return sorted_list
