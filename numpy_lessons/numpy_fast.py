import time
import numpy as np

def python_slow():
    list1 = [i for i in range(200000)]
    list2 = [j**2 for j in range(200000)]

    start_time = time.time()
    list3 = list(map(lambda x, y: x * y, list1, list2))
    end_time = time.time()

    diff_time = end_time - start_time
    print(diff_time)


def numpy_fast():
    array1 = np.array([i for i in range(200000)])
    array2 = np.array([j**2 for j in range(200000)])

    start_time = time.time()
    array3 = array1 * array2
    end_time = time.time()

    diff_time = end_time - start_time
    print(diff_time)

if __name__ == "__main__":
    print("Python slow multiplication:")
    python_slow()
    print("NumPy fast multiplication:")
    numpy_fast()