#1. Remove Duplicates from Sorted Array with Space Coplexity = O(n)

def remove_duplicatee_space(arr):
    n = len(arr)
    if(n == 0 or n == 1):
        return arr

    temp= [0]*n
    pivot= 0
    for last_occurence in range(0, n-1):
        if(arr[last_occurence] != arr[last_occurence+1]):
            temp[pivot]= arr[last_occurence]
            pivot = pivot+1

    temp[pivot] = arr[n-1] 
    return temp[0:pivot+1]  

arr = [1,1,2,2,2,3,4,4,4,5,5]
print(remove_duplicatee_space(arr))



#2. Remove Duplicates from Sorted Array with Space Coplexity = O(1)

def remove_duplicatee_space(arr):
    n = len(arr)
    if(n == 0 or n == 1):
        return arr

    # temp= [0]*n
    pivot= 0
    for last_occurence in range(0, n-1):
        if(arr[last_occurence] != arr[last_occurence+1]):
            arr[pivot]= arr[last_occurence]
            pivot = pivot+1

    arr[pivot] = arr[n-1] 
    return arr[0:pivot+1]  

arr = [1,1,2,2,2,3,4,4,4,5,5]
print(remove_duplicatee_space(arr))             