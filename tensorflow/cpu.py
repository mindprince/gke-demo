from __future__ import print_function
import tensorflow as tf
import time

def get_times(maximum_time):

    device_name = "/cpu:0"
    size_and_time = []
    matrix_sizes = range(500, 50000, 50)

    for size in matrix_sizes:
            print("####### Calculating on the " + device_name + " #######")

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
                return size_and_time

size_and_time = get_times(5)
for size, time in size_and_time:
    print(size, time)
