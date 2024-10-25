from math import factorial

def power_function(a):
    return lambda x: x ** a

def tailor_generator(x):
    n = 0  
    while True:
        # Calculate the next term in the Taylor series
        yield power_function(n)(x) / factorial(n)
        n += 1  

'''
gen = tailor_generator(3) 
sum=0
for _ in range(20):
    sum+=next(gen)
    print(sum)
'''