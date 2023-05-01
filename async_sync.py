# Example of synchronous and asynchronous programming in Python

# Synchronous programming: executing tasks one at a time, in a sequential manner
import time

def task1():
    time.sleep(2)
    print("Task 1 completed")

def task2():
    time.sleep(1)
    print("Task 2 completed")

start_time = time.time()
task1()
task2()
end_time = time.time()

print("Total time taken:", end_time - start_time) # Output: Total time taken: 3.002504825592041

# Asynchronous programming: executing tasks concurrently, without blocking the main thread
import asyncio

async def async_task1():
    await asyncio.sleep(2)
    print("Async task 1 completed")

async def async_task2():
    await asyncio.sleep(1)
    print("Async task 2 completed")

async def main():
    await asyncio.gather(async_task1(), async_task2())

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print("Total time taken:", end_time - start_time) # Output: Total time taken: 2.001
