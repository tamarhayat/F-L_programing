from functools import reduce
f= lambda x: x/2+2   #from the last question

numbers = range(1, 1001)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

f1= lambda acc, x: acc * x
f2= lambda acc, x: f(acc) + x
#צריך לבדוק אם לזה הם התכוונו. או שזה רשימה כלשהי ולא ערך
even_result = reduce(f1,even_numbers)
odd_result =  reduce(f2, odd_numbers)

sum_even = reduce(lambda x,y: x+y, even_numbers)
sum_odd = reduce(lambda x,y: x+y, odd_numbers)

#print(even_result)
#print(odd_result)
#print(sum_even)
#print(sum_odd)