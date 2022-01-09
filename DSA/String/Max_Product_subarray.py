def maxProductSubArrray(A):
    cur_min = A[0]
    cur_max = A[0]
    prev_max = A[0]
    prev_min = A[0]
    result = A[0]

    for i in range(1, len(A)):
        cur_max = max(prev_max * A[i], prev_min * A[i], A[i])
        cur_min = min(prev_max * A[i], prev_min * A[i], A[i])

        result = max(cur_max, result)
        prev_max = cur_max
        prev_min = cur_min

    return result


A = [-6,4,-5,8,-10,0,8]
print(maxProductSubArrray(A))

