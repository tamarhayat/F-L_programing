from math import sqrt

def is_prime(num):
    if num < 2:         # 0,1 is not primes
        return False
    return all(num%i!=0 for i in range(2,int(sqrt(num))+1))  #until and include sqrt(num)


# expect of 5 that have 2 twins so it is special case
def twin(num):
    if is_prime(num+2):
        return num+2
    if is_prime(num-2):
        return num-2
    return None

def range_twins(n):
    return {x: twin(x) for x in range(n) if is_prime(x)}

print(range_twins(9))