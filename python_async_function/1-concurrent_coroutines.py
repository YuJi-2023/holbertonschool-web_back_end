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
    for i in range(len(result_list)):
        for j in range(len(result_list) - i - 1):
            if result_list[j] > result_list[j + 1]:
                result_list[j], result_list[j + 1] =\
                        result_list[j + 1], result_list[j]
    return result_list
