
def sumDigit(n):
    if(n==0):
        return 0
    return sumDigit(int(n/10))+n%10

#print(sumDigit(276))