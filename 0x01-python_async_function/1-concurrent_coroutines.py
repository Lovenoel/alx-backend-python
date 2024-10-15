#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random
n times with the specified max_delay.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times and returns the list of delays.
    The delays should be in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
