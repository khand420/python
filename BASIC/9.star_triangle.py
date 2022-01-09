# TIME COMPLEXITY: loop inside loop thats why O(n2)

            #1.Triangle increasing order
# num = int(input("Enter the Number: "))
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("*", end='')  #end = is used for print value in same line
#     print() #for changin g new line  

            #   1.1   
num = int(input("Enter the Number: "))
for row in range(1, num+1, 2):
    for col in range(1, row+1):
        print("*", end='')  #end = is used for print value in same line
    print() #for changin g new line              


    # 2. Triangle Decreasing order
num = int(input("Enter the Number: "))
for row in range(num, 0, -1):
    for col in range(1, row+1):
        print("*", end='')  #end = is used for print value in same line
    print() #for changin g new line     
