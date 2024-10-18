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
    # Create a list of tasks that each call wait_random with max_delay
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Collect results in the order they complete using asyncio.wait
    sorted_delays = []
    while tasks:
        # Wait for at least one of the tasks to complete
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        # Gather the results of the completed tasks
        for task in done:
            sorted_delays.append(task.result())

    return sorted_delays
