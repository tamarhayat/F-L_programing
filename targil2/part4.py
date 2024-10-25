from functools import reduce
from math import factorial


def power_function(a):
    return lambda x: x**a

def foo(n):
    return map(lambda i:power_function(i),range(n))

def tailor(x,n):
    all=list(map(lambda f,i: f(x)/factorial(i),foo(n),range(n)))
    return reduce(lambda x,y: x+y, all)

print(tailor(3,10000))   
