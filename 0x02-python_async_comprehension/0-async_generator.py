#!/usr/bin/env python3
"""
a coroutine called async_generator that takes no arguments.
loops 10 times, each time asynchronously waits for 1 second,
then yields a random number between 0 and 10. Use the random module.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An async generator that yields random numbers between 0 and 10,
    10 times, with a 1 second pause between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
