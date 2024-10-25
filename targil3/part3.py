def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_tail(a, b, gcd_value=None):
    if gcd_value is None:
        gcd_value = gcd(a, b)
    return abs(a * b) // gcd_value

#print(lcm_tail(6, 4))  
#print(lcm(6, 4)) 
