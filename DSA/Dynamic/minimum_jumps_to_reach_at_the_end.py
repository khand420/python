# By recursion 

def minJumbs(arr, start, end):
    if(start == end):
        return 0

    if(arr[start] == 0):
        return float('infinity')

    min = float('infinity')
    for i in range(start + 1, end + 1):
        if i <= start + arr[start]:
            jumps = minJumbs(arr, i, end)
            if(jumps + 1 < min):
                min = jumps + 1

    return min   


# by dynamic programming

def minJumpsDP(arr):
    if arr[0] == 0:
        return float('infinity')

    end = len(arr)

    dp = [0 for i in range(end)]

    for i in range(1,end):
        dp[i] = float('infinity')
        for j in range(0, i):
            if i <= j + arr[j]:
                dp[i] = min(dp[i], dp[j] + 1) 
    return dp[-1]             