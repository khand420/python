def number():
    num = int(input("Enter the Number: "))
    if(num<0):
        if(num == 0):
            print("Number is Zero")
        else:
            print("Number is Negative")
    else:
        print("Number is Positive")

number()            