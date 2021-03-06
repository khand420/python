def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp 

def partition(A, left, right, pIndex):
    pivot = A[pIndex]
    i = left - 1
    for j in range(left, right):
        if A[j] <= pivot:
            i = i+1
            swap(A, i, j)
    swap(A, i+1, pIndex)
    return i+1

def quickSelect(A, left, right, k):
	# If the list contains only one element, return that element
	if left == right:
		return A[left]
	# select a pIndex between left and right
	pIndex = right
	pIndex = partition(A, left, right, pIndex)
	# The pivot is in its sorted position
	if k == pIndex:
		return A[k]
	# if k is less than the pivot index
	elif k < pIndex:
		return quickSelect(A, left, pIndex - 1, k)
	# if k is more than the pivot index
	else:
		return quickSelect(A, pIndex + 1, right, k)

if __name__ == '__main__':

	A = [7, 4, 6, 3, 9, 1]
	k = 3

	print("Kth smallest element is", quickSelect(A, 0, len(A)-1, k-1))