# T(n) = O(nlogn)

def maxDifference(arr):
    arr = sorted(arr)   #O(nlogn)
    # arr.sort()
    size = len(arr)
    max_diff = -9999*999

    for i in range(size-1):  #O(n)
        if(arr[i+1] - arr[i] > max_diff):
            max_diff = arr[i+1] - arr[i]
    return max_diff

arr = [5,32,45,9,12,18,25]     
print("Maximum difference between elements of array is:",maxDifference(arr))       