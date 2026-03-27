import time
import random
from cecs328pa3 import max_profit

def benchmark():
    # maximum assignment constraints
    n = 200
    W = 400
    U = 400

    values = [random.randint(0, 1000000) for _ in range(n)] # generate random value for specified range 0 - 1000000
    weights = [random.randint(1, 10) for _ in range(n)]
    volumes = [random.randint(1, 10) for _ in range(n)]

    print(f"Benchmark: n={n}, W={W}, U={U}")

    start_time = time.perf_counter()
    result_value, result_indices = max_profit(n, W, U, values, weights, volumes)
    end_time = time.perf_counter()

    duration = end_time - start_time

    print("-" * 30)
    print(f"Max Profit: {result_value}")
    print(f"Number of Items Chosen: {len(result_indices)}")
    print(f"Execution Time: {duration:.4f} seconds")
    print("-" * 30)

    if duration <= 5.0: print("Benchmark Passed: Execution time is within the 5-second limit.")
    else:               print("Benchmark Failed: Execution time exceeds the 5-second limit.")

if __name__ == "__main__":
    benchmark()