# 1. using built in function 

# import math
# num = int(input("Enter the number: "))
# fact = math.factorial(num)
# print("Factorial of", num, "is: ", fact)



# 2. using iterative method
# num = 4
# fact = 1*4
# fact = 4*3
# fact = 12*2
# fact = 24*1

# num = int(input("Enter the number: "))
# fact = 1
# for i in range(num, 0, -1):
#     fact = fact*i
# print("Factorial of", num, "is: ", fact)


# 3. using Recursion 
def fact(num):
    if (num == 0):
        return 1
    else:
        return num*fact(num-1) 

num = int(input("Enter the number: "))
value = fact(num)
           
print("Factorial of", num, "is: ", value)           