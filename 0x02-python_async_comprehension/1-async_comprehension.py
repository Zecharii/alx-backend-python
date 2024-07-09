#!/usr/bin/env python3
from typing import List


from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension 
    and returns them as a list."""
    return [async_num async for async_num in async_generator()]
