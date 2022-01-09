# FILTER 

# def is_even(n):
#     return n%2 == 0

# nums = [3, 2, 6, 5, 2, 9]

# evens = list(filter(is_even, nums))
# print(evens)

# OR 

from functools import reduce


nums = [3, 2, 6, 5, 2, 9]

evens = list(filter(lambda n : n%2==0, nums))
print(evens)
double = list(map(lambda n : n*2, nums))
print(double)
sum = reduce(lambda a,b : a+b, nums)
print(sum)



 
# MAP 