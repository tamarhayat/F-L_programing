from functools import reduce

def add3dicts(d1, d2, d3):
    # union all the dictionaries
    all_keys = set(d1) | set(d2) | set(d3)
    
    # for any key, we will do a tuples, and then we will remove doubles.
    return {
        k: tuple(set(reduce(lambda all,d: all+([d.get(k)] if d.get(k) else []),[d1,d2,d3],[]))) for k in all_keys
    }

'''
#checking: 
d1 = {'a': 1, 'b': 2}
d2 = {'a': 3, 'c': 4}
d3 = {'b': 2, 'c': 5, 'd': 6}

result = add3dicts(d1, d2, d3)
print(result)
'''
