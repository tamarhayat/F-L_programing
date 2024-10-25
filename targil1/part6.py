

def multiply_by_2(x):
    return x*2

def square(x):
    return x*x

def reverse(x):
    return 1/x

operations=[multiply_by_2, square, reverse]

def foo(numbers,operations):
    return{
        op.__name__: list(map(op,numbers)) for op in operations
    }

#print(foo([1,2,3],operations))