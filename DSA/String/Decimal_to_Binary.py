# def DtoB(dec_num):
#     if(dec_num == 0):
#         return
#     else:
#         DtoB(int(dec_num/2))
#         print(dec_num%2, end="")

# DtoB(9)  



# In Combination of both string number
def digit(str):
    size = len(str)

    if(size == 0):
        return
    else:
        last_char = str[size-1]
        digit(str[0:size-1])
        if(last_char.isdigit()):
            DtoB2(int(last_char))
        print()

def DtoB2(dec_num):
    if(dec_num == 0):
        return
    else:
        DtoB2(int(dec_num/2))
        print(dec_num%2, end="") 

digit("l2b325hjl9")              