from concurrent.futures import ProcessPoolExecutor
import math
import random


AMOUNT_OF_MATHS = 8
MAX_WORKERS = 8


def do_maths():
    for i in range(random.randint(1000000, 3000000)):
        final_sqrt = math.sqrt(i)
    return final_sqrt


def main():
    # Context manager defaults to waiting for all procs to complete
    # Same as using the 'wait' function
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = []
        for _ in range(AMOUNT_OF_MATHS):
            futures.append(pool.submit(do_maths))

    for task in futures:
        print(task.result())


if __name__ == "__main__":
    main()
