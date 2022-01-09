# def func(n):
#     if(n>=1):
#         func(n-1)
#         print(n)

# func(3)    


def func(n):
    if(n>=1):
        func(n-1)
        print(n)
        func(n-1)


func(3) 
