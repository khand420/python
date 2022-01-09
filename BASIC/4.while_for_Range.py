#1. while loop

from typing import Collection


i = 0
while(i<5):
    print("khand") 
    i = i+1

# print even time only 
# even = 2
# while(even <= 10):
#     print("Number is Even")
#     even = even+2    

#1.2 sum of even number less than 10
# i = 1
# sum = 0
# while(i<=10):
#     if(0%2 == 0):
#         sum = sum+i
#     i = i+1
# print("The sum of Even Number less than 10:", sum)    


#2. for loop

# multiple of product given in list 
num = [10, 20, 40]
prod= 1
for i in num:
    prod = prod * i
print(prod)    


# 3.Range -> it is a Collection which provides list of values 
# rang(m, n, stepsize)
# m = start value 
# n = last value
# stepsize = +2, +3, -1

num = list(range(20, 0, -2))
print(num)


# range(x) returns a list, that is created in memory with x elements.
# xrange(x) returns an xrange object which is a generator obj which generates the numbers on demand. they are computed during for-loop(Lazy Evaluation).

# For looping, this is slightly faster than range() and more memory efficient.






# Python code to demonstrate range() vs xrange()
# on  basis of return type
 
# initializing a with range()
a = range(1,10000)
 
# initializing a with xrange()
from past.builtins import xrange
x = xrange(1,10000)
 
# testing the type of a
print ("The return type of range() is : ")
print (type(a))
 
# testing the type of x
print ("The return type of xrange() is : ")
print (type(x))


# if you want to write code that will run on both Python 2 and Python 3, use range() as the xrange function is deprecated in Python 3.
# range() is faster if iterating over the same sequence multiple times.
# xrange() has to reconstruct the integer object every time, but range() will have real integer objects. (It will always perform worse in terms of memory however)

