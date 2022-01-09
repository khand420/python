# Maximum Sum SubArray (Kadane's algorithm) With Algorithm

def max_sum_subarray(arr):
    size = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    start= 0; end= 0; pointer= 0

    for i in range(0, size):
        curr_sum = curr_sum + arr[i]
        
        if(max_so_far < curr_sum):
            max_so_far = curr_sum
            start = pointer
            end = i

        if(curr_sum<0):
            curr_sum = 0
            pointer = i+1

    print("Maximum Sum subArray is: ",max_so_far) 
    print("Start Index of window is: ", start) 
    print("End Index  of window is: ",end) 

arr = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
max_sum_subarray(arr)
