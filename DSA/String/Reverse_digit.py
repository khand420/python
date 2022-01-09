def revDigit(str):
    size = len(str)
    if(size == 0):
        return
    else:
        last_char = str[size-1]
        if(last_char.isdigit()):
            print(last_char, end = "")

        revDigit(str[0:size-1])


revDigit("23cod98")
