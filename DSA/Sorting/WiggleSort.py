# def wave(nums):
#     A = sorted(nums)

#     for i in range(0, len(A) - 1, 2):
#         A[i], A[i + 1] = A[i + 1], A[i]
#     return A

# A = [4,2,3,1,5]
# print(wave(A))    


# for repeating num in array
def wiggleSort( nums ):
    if (nums == 0 or len(nums) < 2):
        return
    mid = (len(nums) + 1) // 2
    left = 0
    right = len(nums) - 1
    medium = quickSelect(nums, left, right, mid)
    temp = [0 for i in range(len(nums))]
    s = 0
    e = len(nums) - 1
    for i in range(len(nums)):
        if (nums[i] < medium):
            temp[s] = nums[i]
            s = s + 1
        elif (nums[i] > medium):
            temp[e] = nums[i]
            e = e - 1
    while (s < mid):
        temp[s] = medium
        s = s + 1
    while (e >= mid):
        temp[e] = medium
        e = e - 1
    smallStart = mid - 1
    largeStart = len(nums) - 1

    for i in range(len(nums)):
        if (i % 2 == 0):
            nums[i] = temp[smallStart]
            smallStart = smallStart - 1
        else:
            nums[i] = temp[largeStart]
            largeStart = largeStart - 1
    return nums

def quickSelect(nums, left, right, mid):
    if left == right:
        return nums[left]
    pIndex = right
    pIndex = partition(nums, left, right, pIndex)
    if mid == pIndex:
        return nums[mid]
    elif mid < pIndex:
        return quickSelect(nums, left, pIndex - 1, mid)
    else:
        return quickSelect(nums, pIndex + 1, right, mid)

def partition(nums, left, right, pIndex):
        pivot = nums[pIndex]
        i = left - 1
        for j in range(left, right):
            if nums[j] <= pivot:
                i = i + 1
                swap(nums, i, j)
        swap(nums, i + 1, pIndex)
        return i + 1



def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


nums = [1,3,2,2,3,1]
print(wiggleSort(nums))

