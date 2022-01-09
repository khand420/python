

from RemoveDuplicates import removeDuplicateSpace


arr = [1,4,2,5,2,3,4,1,4,5,2,3]


# 1.Using set functions
# arr1 = list(set(arr))
# print(arr1)


# 2. usin empty array
# lst = []
# for i in arr:
#     if i not in lst:
#        lst.append(i)
# print(lst)  


# 3.usign lambda function
func1  = lambda arr:set(arr)
print(func1)



# 4.Remove dublicate value from dictionary
dict1= {
    'car':["Ford","Toyota","Ford","Toyota"],
    'brand':["Mustang", "Ranz","Mustang","Ranz"]
}

dict2= {}
for key,value in dict1.items():
    dict2[key] = set(value)
print(dict2)    





# 4.Remove dublicate in set using symmetric_difference
set1 = {1,2,4,5}
set2 = {1,2,4,7}

remv = set1.symmetric_difference(set2)
print(remv)
