def mod_pow(x,n,M):
    if(n==0):
        return 1

    elif(n%2==0):
        res = pow(x,n/2)%M
        return (res * res) % M
    else:
        return((x%M) * (pow(x,n-1)%M))%M    


p = mod_pow(7,2,3)
print(p)