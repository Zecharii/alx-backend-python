#!/usr/bin/env python3
import asyncio
import time


from 1-concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n and return the average per call."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
