# lets 

# Red  = 1
# Blue = 2
# Yellow = 3




def sortColor(A):
    size = len(A)
    red = 0
    blue = 0

    for i in range(size):
        if(A[i] == 1 ):
            red = red + 1

        elif(A[i]== 2):
            blue = blue + 1
        
    return [1]*red + [2]*blue + [3]*(size-red-blue)



A = [1,2,3,1,3,2,1,2,3,1]
print(sortColor(A))