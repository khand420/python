def reverse(str_r):
    str1 = str_r[::-1]
    return str1


# str_r = "code2hell"
# print(reverse(str_r))


def reverse_words(str_r):
    n = len(str_r)

    if(n==1):
        return str_r

    str2 = str_r.split(" ")
    size = len(str2)
    rev_all = ""

    for i in range(size):
        rev = reverse(str2[i])
        rev_all = rev_all + rev + " "
    
    d = reverse(rev_all)
    return d.strip

    # print(rev_all)  
    # print(reverse(rev_all))    



str_r = "code2hell is a codding blog"
print(reverse_words(str_r))    