# count no of words in dictionary

# def freqWords():
#     str = input("Enter a String: ")
#     li = str.split
#     d = {}

#     for i in li:
#         if i not in d.keys():
#             d[i]= 0
#         d[i] = d[i]+1

#     print(d)


# freqWords()             




def freq_words():
    str=input("Enter a string: ")
    li=str.split()
    d={}
    print('--->',li)
    for i in li:
        d[i]=d.get(i,0)+1
    print(d)

freq_words()