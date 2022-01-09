def threeSum(arr, target):
    size = len(arr)
    min_diff = abs(arr[0] + arr[1] + arr[2] - target)
    best_till_now = arr[0] + arr[1] + arr[2]

    for i in range(0,size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                new_diff = abs(arr[i] + arr[j] + arr[k] - target)
                if(new_diff < min_diff):
                    min_diff = new_diff
                    best_till_now = arr[i] + arr[j] + arr[k]

    return best_till_now


arr = [-1,1,-4,2]
target = 1
print(threeSum(arr, target))
        
