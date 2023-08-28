#!/usr/bin/env python3
"""an asynchronous coroutine wait_n"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """takes two ints, measure the total execution time for wait_n and\
        return its average time"""
    async def measure():
        total_time = 0.0
        start = time.time()
        await wait_n(n, max_delay)
        end = time.time()
        total_time += end - start
        return total_time

    total_time = asyncio.run(measure())
    return total_time / n
