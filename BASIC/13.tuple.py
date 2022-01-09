# *****LIST                                 TUPLE*****
# 1.mutable                                   1.immutable
# 2.dynamic                                   2.not dynamic           
# 3.slow                                      3.fast      
# 4.operation lik add, insert are applied     4.no functions are applied  

    #  EXAMPLES
emptyTuple = ()

tup1 = (10)
# print(type(tup1))

tup2 = 10,
# print(type(tup2))

tup3 = (20, 30, 40, 50)                     #tuple of integer
tup4 = ("code2hell", "cloud", "python")     #tuple of integer
tup5 = (20, 45, 53, "code2hell", "cloud")    #tuple of mixed value
tup6 = (10, (23, 43),[23, 43])              #tuple of list,integer,tuples-nested tuples



# x = (10, 20,[40,50,60])
# print(x[0])
# print(x[2][0])   
# print(len(x))

# x[2][0]= 30
# print(x[2][0])    #immutable(tuple cannot modified)
# del (x)



# ************ METHODS ***************


#tuple has forward & backword indexing
#     0   1              2             3   forward indexing
#    -4  -3             -2            -1   backword indexing
y = (10, 40.9, ['cloud', 'python'], (60,40))  #nested tuple
# print(y[-1][1])
# print(type(y[-2][1]))


# Slicing
# print("-----Slicing------")

# print(y[:3])   # 0 to upto 2 indexes
# print(y[:-2])  # 0 to -2 indexes
# print(y[1:3])  #1 to 2 indexes
# print(y[::2])  # 0 to end but in even indexes


#Concatination
tup = ("Reena", "Sheena") + ("Meena", "Neena")   
print("The concatination of 2 tuple: ",tup)

tup1 = ((10, 30, 40)*4)
print(tup1)


# Some Experiment on tuple
tup2 =(2,3,4,2,4,5,5,6,7,6,78,84,1,43,12,1)

print(tup2.count(1)) #Frequency of element of given tuple
print(tup2.index(3)) #Index value of given tuple

print(1 in tup2)     # Membership-check the element in tuple
print(9 not in tup2)  

a = sorted(tup2)     #Sort the value of given tuple
print(a)

print(max(tup2))     #Find maximum  value in  tuple
print(min(tup2))     #Find minimum value in  tuple
print(sum(tup2))     #sum of tuple
