# Time Complexity = O(n^2)
# Space Complexity = O(1)



def bubbleSort(array):
    

#   for i in range(len(array)):
  for i in range( len(array)-1, 0, -1 ):

    # for j in range(0, len(array) - i - 1):
    for j in range(i):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)








# def bubbleSort(elements):
#     size = len(elements)


#     for i in range(size-1):
#         if elements[i] > elements[i+1]:
#             temp = elements[i]
#             elements[i] = elements[i+1]
#             elements[i+1] = temp




# if __name__ == "__main__":
#     elements = [5,9,2,1,67,34.80,34]
#     bubbleSort(elements)
#     print(elements)









# you can use this to sort strings too
# def bubble_sort(elements):
#     size = len(elements)

#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):
#             if elements[j] > elements[j+1]:
#                 tmp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = tmp
#                 swapped = True

#         if not swapped:
#             break


# if __name__ == '__main__':
#     elements = [5,9,2,1,67,34,88,34]
#     elements = [1,2,3,4,2]
#     elements = ["mona", "dhaval", "aamir", "tina", "chang"]

#     bubble_sort(elements)
#     print(elements)    