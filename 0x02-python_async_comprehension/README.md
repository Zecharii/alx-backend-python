# Python - Async Comprehension
This project is part of the short specializations course of the Software Engineering programme at ALX. It aims to teach us about Asynchronous Comprehension in Python.

## Learning Objectives
At the end of this project, we are expected to know:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements
- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7)
- All code used the `pycodestyle` style (version 2.5.x)
- The length of your files will be tested using `wc`
- All modules and functions have a real sentence documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions and coroutines are type-annotated.

## Tasks
| Files | Description |
|-------|-------------|
| `0-async_generator.py` | Coroutine called async_generator that loops 10 times, each time asynchronously waits 1 second, then yields a random number between 0 and 10. |
| `1-async_comprehension.py` | Coroutine called async_comprehension that collects 10 random numbers using an async comprehensing over async_generator, then returns the 10 random numbers. |
| `2-measure_runtime.py` | Coroutine measure_runtime that executes async_comprehension four times in parallel using asyncio.gather and measures the total runtime. |
