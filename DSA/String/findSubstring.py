# base of dynamic programming
def substring(str1, n):
    for i in range(n):
        for j in range(i+1,n+1):
            print(str1[i:j])


str1 = "KHAN"
n = len(str1)
substring(str1, n)              