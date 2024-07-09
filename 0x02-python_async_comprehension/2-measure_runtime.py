#!/usr/bin/env python3
import asyncio
import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of executing async_comprehension 
    four times in parallel.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
