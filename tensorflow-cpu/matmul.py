from __future__ import print_function
import tensorflow as tf
import time
import sys

# "/cpu:0" for CPU
# "/gpu:0" for GPU
device_name = sys.argv[1]

# Do so many iterations
maximum_iteration = int(sys.argv[2])

matrix_sizes = range(500, 500 + 10*maximum_iteration, 10)

# If the time taken for an iteration exceeds this many seconds, we quit
maximum_time = 10

# This contains tuples of matrix size and time taken
size_and_time = []

for size in matrix_sizes:
    shape = (size, size)
    data_type = tf.float16
    with tf.device(device_name):
        r1 = tf.random_uniform(shape=shape, minval=0, maxval=1, dtype=data_type)
        r2 = tf.random_uniform(shape=shape, minval=0, maxval=1, dtype=data_type)
        dot_operation = tf.matmul(r2, r1)

    with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as session:
        start_time = time.time()
        result = session.run(dot_operation)
        time_taken = time.time() - start_time
        size_and_time.append((size, time_taken))

    if time_taken > maximum_time:
        break

print("####### Calculating on the " + device_name + " #######")
for size, time in size_and_time:
    print(size, time)
