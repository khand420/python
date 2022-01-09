# T(n) = O(nlogn)

def minimumDifference(arr):
    arr = sorted(arr)   #O(nlogn)
    # arr.sort()
    size = len(arr)
    min_diff = 9999*999

    for i in range(size-1):  #O(n)
        if(arr[i+1] - arr[i] < min_diff):
            min_diff = arr[i+1] - arr[i]
    return min_diff

arr = [5,32,45,9,12,18,25]     
print("Maximum difference between elements of array is:",minimumDifference(arr))       