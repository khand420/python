from math import sqrt

def PrimeNumber(num):
    if(num > 1):
        # for i in range(2,num):  #O(n)
        # for i in range(2,int(num/2)):  #O(n/2)
        for i in range(2,int(sqrt(num))+1):  #O(nlogn)
            if(num%i == 0):
                return False
        return True


is_prime = PrimeNumber(49)
if(is_prime):
    print("Prime Number")
else:
    print("Not a Prime Number")



#2. Sieve of Eratosthenes | Fastest way for Prime Number | Facebook
def sieve_prime(num):
    prim_arr = [1] * (num+1)
    prim_arr[0] = 0
    prim_arr[1] = 0

    # for i in range(2,num):
    for i in range(2,int(sqrt(num))+1):    #O(nlogn)
        if(prim_arr[i]==1):
            j=2
            while(i*j<num+1):
                prim_arr[j*i] = 0
                j = j+1
    return prim_arr


print(sieve_prime(15))
