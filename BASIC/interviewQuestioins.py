# 1. Find index of anagrams?

# step:
# 1.create a dictionary
# 2.if sorted word not in dictionary, set word as key & index as value
# 3.if sorted word in dictionary , append index for word


def anagram(A):
    if(A==None):
        return
    else:
        dict={}
        for i in range(len(A)):
            word= ''.join(sorted(A[i]))
            if(word not in dict):
                dict[word] = [i+1]    
            else:
                dict[word].append(i + 1)
        return dict

A = ["cat", "dog", "god", "tca", "act"]
print(anagram(A))                    



# 2.Remove duplicates in python 

arr = [2, 3, 5, 5, 1, 3, 5, 7, 8, 2, 0, 9]

# 2.1 using set() function 
set1 = list(set(arr))
print("Remove duplicates using set ",set1)

# 2.2 using array[]
arr2=[]
for i in arr:
    if(i not in arr2):
        arr2.append(i)
print("Remove duplicates using array: ",arr2)        

# 2.3 using lambda function
remDuplicate = lambda arr:list(set(arr))
print("using lambda function: ",remDuplicate(arr))

# 2.4 using dictionary
dict1 = {
    'car':["Ford","Toyota","Ford","Toyota"],
    'brand':["Mustang","Ranz", "Mustang", "Ranz"]
}

dict2={}

for key, value in dict1.items():
    dict2[key] = set(value)
print(dict2)

# Symmetric difference - Remove duplicate elements
set1 ={1,3, 4, 5}
set2 = {2,1,5,7}

remv = set1.symmetric_difference(set2)
print(remv)


# 3. Find the maximum element in list[]
def maximum(arr):
    max = arr[0]               #zero index is 62
    size = len(arr)
    for i in range(size):
        if(arr[i]>max):
            max=arr[i]
    return max

arr=[62, 43, 35, 6, 65, 90, 19]
print("Maximum element: ",maximum(arr))
 
# 3. Find the minimum element in list[]
def minimum(arr):
    min= arr[0]                 # min = 63    #zero index is 62
    size = len(arr)             #size= 7
    for i in range(size):       #i = 0  
           #    62<43
        if(arr[i] < min):      # arr[i] = arr[0] = 63
            min = arr[i]
          # min = 43
    return min

arr=[62, 43, 35, 6, 65, 90, 19]
print("Minimum element: ",minimum(arr))
