

# def prime_num(num):
#     if(num>1):
#         for i in range(2,num):
#             if(num%i==0):
#                 return False
#         return True

# num = int(input("Enter the Number: "))
# is_prime = prime_num(num)
# if(is_prime):
#     print("Prime Number")
# else:
#     print("Not a Prime Number")




# reduce time complexity using sqrt over number
from math import sqrt
def prime_num(num):
    if(num>1):
        for i in range(2,int(sqrt(num))+1):
            if(num%i==0):
                return False
        return True

num = int(input("Enter the Number: "))
is_prime = prime_num(num)
if(is_prime):
    print("Prime Number")
else:
    print("Not a Prime Number")




# Sieve of Eratosthenes | Fastest way of Prime Number
# T(n): O(nlogn)
def sieve_prime(num):
    prime_arr=[1]*(num+1)
    prime_arr[0]=0
    prime_arr[1]=0
    
    for i in range(2,int(sqrt(num))+1):
    # for i in range(2, num):
        if(prime_arr[i]==1):
            j=2
            while(i*j<num+1):
               prime_arr[j*i]=0
               j=j+1
    return prime_arr

        
print(sieve_prime(15))

