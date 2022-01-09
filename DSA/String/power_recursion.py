# method 1:
# TimeComplexity = O(n)

def power_recursion(x, n):
    if(n == 0):
        return 1
    else:
        return x * pow(x,n-1)

print(power_recursion(2,5))



# method 2
# TimeComplexity = O(logn) better than 1st one


def power_recursion(x, n):
    if(n == 0):
        return 1
    elif(n%2==0):
        res= x * pow(x,n/2)
        return res * res    
    else:
        return x * pow(x,n-1)


print(power_recursion(2,5))

