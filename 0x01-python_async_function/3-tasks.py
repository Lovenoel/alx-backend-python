#!/usr/bin/env python3

"""
a function task_wait_random that takes an integer max_delay
and returns a asyncio.Task.
""
import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
