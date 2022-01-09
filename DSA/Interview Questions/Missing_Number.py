def SummationMethod(a):
    Lnum = a[-1]
    sum1 = 0
    total = Lnum*(Lnum+1)//2    #7(7+1)//2 = 28 sum of natural number

    sum1 = sum(a) #sum of array a

    print(total- sum1)




def XOR_method(a):
    n = len(a)
    xor_a = a[0]
    for index in range(1,n):
        xor_a = xor_a ^ a[index]

    x2 = 0
    for index in range(1, n+2):
        x2 = x2 ^ index
    print(xor_a ^ x2)    





a= [1,2,3,4,6,7]

SummationMethod(a)  
XOR_method(a)