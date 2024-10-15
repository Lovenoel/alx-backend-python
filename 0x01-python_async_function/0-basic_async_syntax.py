#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay and returns it.
    The delay is a float between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
