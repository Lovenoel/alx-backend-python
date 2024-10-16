#!/usr/bin/env python3
"""
a coroutine called async_comprehension that takes no arguments.
but collects 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehending over async_generator
    and returns the list of numbers.
    """
    return [i async for i in async_generator()]
