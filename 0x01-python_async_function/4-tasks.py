#!/usr/bin/env python3
import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times and return the list of delays
    in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
