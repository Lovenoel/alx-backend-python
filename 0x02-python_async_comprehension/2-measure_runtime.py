#!/usr/bin/env python3
"""
Imports async_comprehension and writes a measure_runtime coroutine
that will execute async_comprehension four times in parallel using
asyncio.gather. measure_runtime should measure the total runtime
and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel, measures
    the total runtime, and returns it.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())
    end_time = time.perf_counter()

    return end_time - start_time
