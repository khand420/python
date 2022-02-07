num = int(input())

result = 0
maximum = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0

    num //= 2

print(maximum)



# if __name__ == '__main__':
#     n = int(input())

#     rmd = []
    
#     while n > 0:
#         rm = n % 2
#         n = n//2
#         rmd.append(rm)
    
#     count,result = 0,0
    
#     for i in range(0,len(rmd)):
#         if rmd[i] == 0:
#             count = 0
#         else:
#             count +=1
#             result = max(result,count)
    
#     print(result)