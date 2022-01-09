
def findPivot(left, right, arr):
    if(left > right):
        return -1
    if(left == right):
        return left

    mid = int(left + (right-left)//2)
    if(mid<right and arr[mid] > arr[mid+1]):
        return mid+1 

    else:
        if(arr[left]>arr[mid]):
            return findPivot(left,mid,arr)
        else:
            return findPivot(mid+1, right, arr)


def pivotSearch(n, key, arr):
    pi = findPivot(0,n-1, arr)
    if(pi == -1):
        return pivotSearch(0,n-1,key,arr)

    if(arr[pi] == key):
       return pi

    if(arr[pi] <= key and key > arr[n-1]):
        return pivotSearch(0,pi-1,key,arr)









A = [7,9,11,13,15,17,19,1,3,5]
key = 9
n = len(A)
print(pivotSearch(n,key,A))


