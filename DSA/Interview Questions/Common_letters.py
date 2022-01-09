def commonLatters():
    str1 = input("Enter First String: ")
    str2 = input("Enter Second String: ")

    s1 = set(str1)
    s2 = set(str2)
    # print(s1)
    # print(s2)

    lst = s1 & s2
    print("Common latter between two string: ",lst)



commonLatters()