# FUNCTIONS:- It is  a group of statement that perfom specific task
            #   it avoids repetition and makes code reusable


# DOCTSTRING - we generally use triple quotes so that docstring can extend upto multiple lines.
# for example
""" Hello, my name is Docstring """


# example1

def evenOdd(x):
    '''even odd funtion '''
    if (x%2== 0):                  #function defination
        print("Even")
    else:    
        print("Odd") 

evenOdd(3)                           #function call 



# for printing Doc String 
print(evenOdd.__doc__)



# example2
def absolute_value(num):
    if(num >= 0):
        return num
    else:
        return -num

print("Enter the number to know positive or negative")
result1=absolute_value(2)
result2=absolute_value(-4)

print(result1)
print(result2)



# Buit in funtions
'''

Function	Description

abs()	Returns the absolute value of a number
all()	Returns True if all items in an iterable object are true
any()	Returns True if any item in an iterable object is true
ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	Returns the binary version of a number
bool()	Returns the boolean value of the specified object
bytearray()	Returns an array of bytes
bytes()	Returns a bytes object
callable()	Returns True if the specified object is callable, otherwise False
chr()	Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()	Returns the specified source as an object, ready to be executed
complex()	Returns a complex number
delattr()	Deletes the specified attribute (property or method) from the specified object
dict()	Returns a dictionary (Array)
dir()	Returns a list of the specified object's properties and methods
divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	Evaluates and executes an expression
exec()	Executes the specified code (or object)
filter()	Use a filter function to exclude items in an iterable object
float()	Returns a floating point number
format()	Formats a specified value
frozenset()	Returns a frozenset object
getattr()	Returns the value of the specified attribute (property or method)
globals()	Returns the current global symbol table as a dictionary
hasattr()	Returns True if the specified object has the specified attribute (property/method)
hash()	Returns the hash value of a specified object
help()	Executes the built-in help system
hex()	Converts a number into a hexadecimal value
id()	Returns the id of an object
input()	Allowing user input
int()	Returns an integer number
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()	Returns an iterator object
len()	Returns the length of an object
list()	Returns a list
locals()	Returns an updated dictionary of the current local symbol table
map()	Returns the specified iterator with the specified function applied to each item
max()	Returns the largest item in an iterable
memoryview()	Returns a memory view object
min()	Returns the smallest item in an iterable
next()	Returns the next item in an iterable
object()	Returns a new object
oct()	Converts a number into an octal
open()	Opens a file and returns a file object
ord()	Convert an integer representing the Unicode of the specified character
pow()	Returns the value of x to the power of y
print()	Prints to the standard output device
property()	Gets, sets, deletes a property
range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	Returns a readable version of an object
reversed()	Returns a reversed iterator
round()	Rounds a numbers
set()	Returns a new set object
setattr()	Sets an attribute (property/method) of an object
slice()	Returns a slice object
sorted()	Returns a sorted list
staticmethod()	Converts a method into a static method
str()	Returns a string object
sum()	Sums the items of an iterator
super()	Returns an object that represents the parent class
tuple()	Returns a tuple
type()	Returns the type of an object
vars()	Returns the __dict__ property of an object
zip()	Returns an iterator, from two or more iterators

'''

# 1.  dir() - returns all properties and methods, even built-in properties which are default for all object
num1 = [1,3,6,7,8]
print(dir(num1))

str1 = "Code2hell is the best coding blog"
# print(dir(str1))

dict1 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
# print(dir(dict1))


# 2.  divmod() - take two numbers and returns a pair of numbers consisting of their quotient and remainder
# if x and y are two integers, the return value is (x/y, x%y)
                                                  #  Q ,  R
print(divmod(17, 4))       #always return in tuple. Quotient = 4, Remainder 1                                           


# 3.Enumerate() method adds a counter to an iterable and return it in a form of enumerate object 
# syntax:- 
#         enumerate(iterable, start=0)

number = [1, 2, 3, 4, 5]
for index, num in enumerate(number):
    print("index", index,"has value", num)




# ----------------Introduction to *args and **kwargs in Python--------------
# In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:

# 1.*args (Non Keyword Arguments)
# 2.**kwargs (Keyword Arguments)

# Note 
# *args and **kwargs are special keyword which allows function to take variable length argument.
# *args passes variable number of non-keyworded arguments list and on which operation of the list can be performed.
# **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
# *args and **kwargs make the function flexible.    



# 1.*args (Non Keyword Arguments)
# def adder(x,y,z):
#     print("sum:",x+y+z)

# adder(5,10,15,20,25)

# example2
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

# 2.**kwargs (Keyword Arguments)
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)





# Lambda Function : Anonymous function we use instead main function
def data(a,b):         #use def key, multiline code
    return a+b
  
add = lambda a, b: a+b      # use lambda key, one line code
print(add(4,5))

twice = lambda x:x*2
# print(type(twice))
print(twice(5))


num = [1,2,3,4,5,6,7,8,9]

even_list = list(filter(lambda val:val%2==0, num))    #lambda with filter funtion
print(even_list)

# cube = list(map(lambda value: value*value*value, num))   #lambda with map funtion
# square = list(map(lambda value: value*value, num))
# print(cube)
# print(square)

# or 

def cube(value):
    return pow(value,3)

def sq(value):
    return pow(value,2)

methods= [sq,cube]

for i in range(10):
    value = list(map(lambda x:x(i), methods))
    print(value)


# for reduce()
def product(a,b):
    return a*b

from functools import reduce
prod = reduce(product, num)
print("Product of numbers are: ", prod)



# -----RECURSION----------
# it is calling a function with in a function 
# it moves
# T to B
# L to R


# SPACE COMPLEXITY:
# n = (n+1)m
# space = O(mn)
#         O(n)

# TIME COMLEXITY:
# T(n) = T(n-1) + 1, n>=1

# solve
# T(n-1) = T(n-1) + 1  ---------(1)
# T(n-1) = T(n-2) + 1  ---------(2)
# T(n-1) = T(n-3) + 1              
# ----------------------------
# T(n) = [T(n-2)+1]
#      =T(n-2)+2
#      =[T(n-2)+1]+2
# T(n) =T(n-3)+3

#    =T(n-k)+k
#    =k=n
#    =T(n-n)+n  = O(n) 





# recursion with inside one function 
# def func(num):
#     if(num>=1):
#        func(num-1)
#        print(num)

# func(3)

# recursion with inside two function 
def func2(n):
    if(n>=1):
       func2(n-1)
       print(n)
       func2(n-1)

func2(3)       
