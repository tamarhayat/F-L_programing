from functools import reduce
import time

f=lambda x: x/2+2

#1
l=list(map(f,range(1,10000)))

#2
def sum_by_reduce(l):
    return reduce(lambda x,y:x+y,l)

#3
def iterative_sum(l):
    total = 0
    for num in l:
        total += num
    return total


#measure the times and equal between them
start_time1 = time.time()
iterative_result = iterative_sum(l)
end_time1 = time.time()
print(f"imperative {end_time1-start_time1}")

start_time = time.time()
non_iterative_result = sum_by_reduce(l)
end_time = time.time()
print(f"non_imperative {end_time-start_time}")

#4
all_in_one = sum(map(f, range(1, 10000)))

#print(all_in_one)