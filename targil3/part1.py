def create_tuple(n):
    if n == 1:
        return (1,)
    return create_tuple(n - 1) + (n,)
    


def create_tuple_tail(n, acc=()):
    if n == 0:
        return acc
    return create_tuple_tail(n - 1, (n,) + acc)

#print(create_tuple(1000))
#print(create_tuple_tail(1000))