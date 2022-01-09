# def CommonElement_in_2List(list1, list2):
#     common = []
#     count = 0
    
#     for i in list1:
#         for j in list2:
#             if( i== j):
#                 common.append(i)
#                 count = count+1

#     print(common)
#     print("Common element in both list is: ", count) 


# using dictionary
def CommonElement_in_2Dict(list1, list2):
    dict1={}
    for element in list2:
        dict1[element] = 1
    count = 0

    for i in list1:
        if dict1.get(i) != None:
            print(i)
            count = count+1 
    print("Common element in both list is: ", count)            

l1 = [2,4,6,8,10,12,14]
l2 = [3,6,9,12,15,18]

# CommonElement_in_2List(l1,l2)
CommonElement_in_2Dict(l1,l2)



