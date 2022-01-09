# Time Complexities

# Best case complexity: O(1)
# Average case complexity: O(log n)
# Worst case complexity: O(log n)

# The space complexity of the binary search is O(1)


# 1.Simple BinarySearch 


def binarySearch(arr, element, low, high):
    while(low<=high):
        mid = low + (high-low)//2

        if (arr[mid]==element):
            return mid

        elif(arr[mid]<element):
            low = mid+1

        else:
            high=mid-1
    return -1

arr=[2,5,6,9,23,56]
element = 9
result = binarySearch(arr, element, 0, len(arr)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")


# 2.1 Integer Square Root | Data Structures
def sqrt(num):
    if(num==0):
        return 0

    low=1
    high= num // 2

    while(low<=high):
        mid = low+(high-low)//2
        if(mid*mid == num):      #square mid = num
            return mid

        if(mid*mid < num):
            low = mid+1
            ans = mid   

        else:
            high=mid-1
    return ans   

print(sqrt(18))


# 2.2 Precision Square Root | Data Structures
def sqrt(num, precis):
    if(num==0):
        return 0

    low=1
    high= num // 2

    while(low<=high):
        mid = low+(high-low)//2
        if(mid*mid == num):      #square mid = num
            return mid

        if(mid*mid < num):
            low = mid+1
            ans = mid   

        else:
            high=mid-1

# presicion
    increment = 0.1
    for i in range(0, precis):
        while(ans * ans <= num):
            ans+=increment

        ans = ans-increment
        increment = increment
        increment = increment/10
    return ans            

print(sqrt(18,2))





# 3.Painter Partition Problem | Google Interview Question | Binary Search | InterviewBit Problem 
class PPP:
    def paint(self, A, B, C):
        start=max(C)
        end=sum(C)
        
        while(start<=end):
            mid=(start+end)//2
            painter=1
            board=0
            for brush in C:
                if (board+brush)>mid:
                    painter=painter+1
                    board=brush
                else:
                    board=board+brush
            if painter<=A:
                end=mid-1
            else:
                start=mid+1
        return (start*B)% 10000003

    





