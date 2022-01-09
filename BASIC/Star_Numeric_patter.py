# pattern 1
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# num = int(input("Enter the number: "))

# for row in range(1, num):
#     for col in range(row, 0, -1):
#         print(col, end=" ")
#     print()    



# pattern 2
#     1
#    2 2
#   3 3 3
#  4 4 4 4

# num = int(input("Enter the number: "))
# space=4

# for row in range(1, num):
#     for spce in range(1, space+1):
#         print(" ", end="")
#     for col in range(1, row+1):
#         print(row, end=" ")
#     print() 
#     space= space-1



# pattern 3
#  5 5 5 5 5
#   4 4 4 4
#    3 3 3
#     2 2
#      1


num = int(input("Enter the number: "))
space = 0

for row in range(num, 0, -1):
    for spce in range(0, space+1):
        print(" ",end="")
    for col in range(1, row+1):
        print(row, end=" ")
    print()
    space = space+1        

       
