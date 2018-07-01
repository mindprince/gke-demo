import torch
import time
import sys

# "cpu" for CPU
# "cuda" for GPU
device = sys.argv[1]

# Do so many iterations
maximum_iteration = int(sys.argv[2])

matrix_sizes = range(500, 500 + 10*maximum_iteration, 10)

# If the time taken for an iteration exceeds this many seconds, we quit
maximum_time = 10

# This contains tuples of matrix size and time taken
size_and_time = []

for size in matrix_sizes:
    r1 = torch.randn(size, size, device=device)
    r2 = torch.randn(size, size, device=device)

    start_time = time.time()
    torch.matmul(r2, r1)
    time_taken = time.time() - start_time
    size_and_time.append((size, time_taken))

    if time_taken > maximum_time:
        break

print("####### Calculating on the " + device + " #######")
for size, time in size_and_time:
    print(size, time)
