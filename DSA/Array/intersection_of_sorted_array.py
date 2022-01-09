
def intersect(A,B):
    L = len(A)
    R = len(B) 

    list = []
    i = 0
    j = 0

    while(i<L and j<R):
        if(A[i] == B[j]):
            list.append(A[i])
            i = j+1
            j = j+1

        if(A[i] < B[j]):
            i = i+1
        
        if(A[i]>B[j]):
            j=j+1

    return list

A = [1,2,3,3,4,5,6]
B = [3,3,5]

# print(intersect(A, B))