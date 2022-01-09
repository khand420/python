
# function
def Search(arr, size, key):
    for i in range(0, size):
        if(arr[i] == key):
            return i
    return -1


# Drived Code
arr =[2, 4, 6, -2, 43]
key = -2
size = len(arr)

# function call
result = Search(arr, size, key)

if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

