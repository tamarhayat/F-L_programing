
def sum(l):
    if not l:
        return 0
    return l[0] + sum(l[1:])

def sum_tail(l, count=0):
    if not l:
        return count
    return sum_tail(l[1:], l[0] + count)

'''
result = sum([1, 2, 3, 4])
print(result)

result = sum_tail([1, 2, 3, 4])
print(result)
'''