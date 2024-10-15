#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random
n times with the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times and returns the list of delays.
    The delays should be in ascending order.
    """
    delays = []
    tasks = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]  # Create n tasks
    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert delay into the correct position to keep the list sorted
        if not delays:
            delays.append(delay)
        else:
            for i, d in enumerate(delays):
                if delay < d:
                    delays.insert(i, delay)
                    break
                else:
                    delays.append(delay)
    return delays
