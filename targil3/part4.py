
def isPalindrome(n):
    n_str=str(n)
    if len(n_str)<=1:
        return True
    return n_str[0]==n_str[-1] and isPalindrome(int(n_str[1:-1]))

def isPalindrome_tail(n, left=0):
    n_str = str(n)
    right = len(n_str) - 1 - left
    
    if left >= right:
        return True
    if n_str[left] != n_str[right]:
        return False
    
    return isPalindrome_tail(n, left + 1)



print(isPalindrome_tail(45354))