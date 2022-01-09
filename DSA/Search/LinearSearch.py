def LinearSearch(list1, element):
    for i in range(len(list1)):   #i used to go each index of a given list
        if(element==list1[i]):
            print("Element is found at index", i)
            break
    else:
        print("Element is not found !")

list1= [3,4,5,7,8,87,35,78,]
element= 23

print(LinearSearch(list1, element))     


# OR


# def linearSearch(array, n, x):

#     # Going through array sequencially
#     for i in range(0, n):
#         if (array[i] == x):
#             return i
#     return -1


# array = [2, 4, 0, 1, 9]
# x = 1
# n = len(array)
# result = linearSearch(array, n, x)
# if(result == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ", result)





# 2.search for repeated element in list 

# def RLSearch(list1, element2):
#     list2 = []
#     flag = False

#     for i in range(len(list1)):
#         if(element2==list1[i]):
#             flag = True
#             list2.append(i)

#     if(flag == True):
#         for i in list2:
#             print("Element",element2,"is found at index: ",i)

#     else:
#         print("Element is not found !")

# list2= [3,4,5,7,3,3,8,87,35,3,78,]
# element2= int(input("Enter the number: "))

# print(RLSearch(list2, element2)) 

