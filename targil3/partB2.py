from math import sqrt

#I take this func from targil 1
def is_prime(num): 
    if num < 2:         # 0,1 is not primes
        return False
    return all(num%i!=0 for i in range(2,int(sqrt(num))+1))  #until and include sqrt(num)


 #I use here in loop although it isnt good for a functional programing because it is infinity
def generate_primes():
    num = 2  
    while True:
        if is_prime(num):
            yield num  # Yield the next prime number
        num += 1  

'''
#an example
gen = generate_primes()
for _ in range(10):
    print(next(gen))
'''