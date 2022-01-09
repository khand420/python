
# TimeComplexity = O(nlogn)
# SpaceComplexity = O(1)

def twoSum(arr, sum):
    arr.sort()         #O(nlogn)
    left = 0
    right = len(arr)-1
    while(left <= right):           # O(n)
        if(arr[left] + arr[right] > sum):
            right = right -1

        elif(arr[left] + arr[right] < sum):
            left = left+1

        elif(arr[left] + arr[right] == sum):
            print("Value of pairs are: ", arr[left], "&", arr[right])
            right = right-1
            left = left+1


arr = [5,7,4,3,9,8,19,21]
sum = 17
twoSum(arr, sum)