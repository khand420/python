# Time Comlexity  = O(nlogn)
# Space Complexity = O(1)



def twoSum(arr, sum):
    arr.sort()     #TC = O(nlogn) -> Best case

    left = 0
    right = len(arr)-1

    while(left <= right):   #TC = O(n)
        if(arr[left] + arr[right] > sum):
            right = right -1

        elif(arr[left] + arr[right] < sum):
            left = left +1

        elif(arr[left] + arr[right] == sum):
            print("Values of pair are", arr[left], "&", arr[right])
            right = right -1
            left = left -1        


arr = [5,7,4,3,9,19,21]
sum = 17
twoSum(arr, sum)            





def twosum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<=right):
        if(arr[left]+arr[right]>sum):
            right=right-1
        elif(arr[left]+arr[right]<sum):
            left=left+1
        elif(arr[left]+arr[right]==sum):
            print("Values of pair are",arr[left],"&", arr[right])
            right=right-1
            left=left+1

def twosum_hashmap(arr,sum):
    dict={}
    for i in range(len(arr)):
        if(sum - arr[i] in dict):
            return [sum-arr[i],arr[i]]
        elif(arr[i] not in dict):
            dict[arr[i]]=i


arr=[5,7,4,3,9,8,19,21]
sum=17
s=twosum_hashmap(arr,sum)
print(s)

