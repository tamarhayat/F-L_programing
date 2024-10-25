import time
import sys

#A

# Create array without lazy evaluation (eager)
def create_array_not_lazy():
    start_time = time.time()
    arr = [x for x in range(10001)]  # Create a full list (eager)
    execution_time = time.time() - start_time
    size = sys.getsizeof(arr)  # Get memory size of the list
    return arr, execution_time, size

arr, exec_time, size = create_array_not_lazy()
print(f"Not lazy execution time: {exec_time}")
print(f"Memory size: {size}")

# Create array with lazy evaluation (using a generator)
def create_array_lazy():
    start_time = time.time()
    arr = (x for x in range(10001))  # Create a generator (lazy)
    execution_time = time.time() - start_time
    size = sys.getsizeof(arr)  # Get memory size of the generator
    return arr, execution_time, size

arr_lazy, exec_time_lazy, size_lazy = create_array_lazy()
print(f"Lazy execution time: {exec_time_lazy}")
print(f"Memory size: {size_lazy}")

#B
def first_5000_not_lazy(arr):
    start_time = time.time()
    new_arr = arr[:5000]  # Regular slicing on a list
    execution_time = time.time() - start_time
    size = sys.getsizeof(new_arr)  # Get memory size of the sliced list
    return new_arr, execution_time, size

new_arr_not_lazy, exec_time_not_lazy, size_not_lazy = first_5000_not_lazy(arr)
print(f"Not lazy 5000 execution time: {exec_time_not_lazy}")
print(f"Memory size: {size_not_lazy}")
print(f"Type: {type(new_arr_not_lazy)}")

def first_5000_lazy(arr):
    start_time = time.time()
    new_arr = list(map(lambda x: x[1], zip(range(5000), arr)))  #take the first 5000 
    
    execution_time = time.time() - start_time
    size = sys.getsizeof(new_arr) 
    return new_arr, execution_time, size

# Use the lazy array (generator)
new_arr_lazy, exec_time_lazy_5000, size_lazy_5000 = first_5000_lazy(arr_lazy)
print(f"Lazy 5000 execution time: {exec_time_lazy_5000}")
print(f"Memory size: {size_lazy_5000}")
print(f"Type: {type(new_arr_lazy)}")
