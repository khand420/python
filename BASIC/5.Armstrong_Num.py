
# 1634, 153
# no = 4

# 4**4 =  256
# 3**4 =   81
# 6**4 = 1296
# 1**4 =    1
#        +
# --------------
# total = 1634 -> it is Armstrong number


num  = int(input("Enter a number: "))

x = num
n = len(str(num))
sum = 0 
while(num>0):
    rem=num%10    #reversing a number
    sum = sum+rem**n
    print(rem)
    num = num //10
if(x==sum):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")        