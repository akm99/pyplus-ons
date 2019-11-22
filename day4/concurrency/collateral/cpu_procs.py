"""
Purpose of this example is to demonstrate multiple processes
(Python instances) being spawned.

Use top or activity/system monitor to see multiple instances
of Python being ran.
"""
from concurrent.futures import ThreadPoolExecutor, wait
import math
import random


AMOUNT_OF_MATHS = 20
MAX_WORKERS = 8


def do_maths():
    for i in range(random.randint(1000000, 3000000)):
        final_sqrt = math.sqrt(i)
    return final_sqrt


def main():
    pool = ProcessPoolExecutor(max_workers=MAX_WORKERS)
    futures = []
    for _ in range(AMOUNT_OF_MATHS):
        futures.append(pool.submit(do_maths))

    wait(futures)

    for task in futures:
        print(task.result())


if __name__ == "__main__":
    main()
