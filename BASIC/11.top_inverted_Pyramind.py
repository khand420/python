# complete TIME COMPLEXITY = O(n^2)

# num = int(input("Enter the number: "))
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("*", end= " ")
#     print()


#    PYRAMIND 
# num = int(input("Enter the Number: ")) #num= 5
# for row in range(1, num+1):           #row = 1
#     for col in range(1, num-row+1):   #col(1, 5-1+1)
#         print(end=" ")                #col(1, 5)
#     for col in range(1, row+1):       #col(1,2,3,4) 4 spaces overhere
#         print("*", end=" ")
#     print()    


    #   INVERSE PYRAMIND 
num = int(input("Enter the Number: "))
#only change range(num,0, -1)                          #num= 5
for row in range(num,0, -1):          #row = 5
    for col in range(1, num-row+1):   #col(1, 5-5+1)
        print(end=" ")                #col(1, 1)
    for col in range(1, row+1):       #col(0) 0 spaces overhere
        print("*", end=" ")
    print()      