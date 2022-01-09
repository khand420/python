from typing import Counter


def first_non_repeating(str_r):
    dict = {}
    size = len(str_r)

    #    using dictionary
    for i in range(size):
        key = str_r[i]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] = dict[key] +1
    
    # for key, value in dict.items():
    #     if(value == 1):
    #         print(key, value)
    #         break
       


    #    using array 
    counter = 0
    for index in range(len(str_r)):
        if(dict[str_r[index]] ==1):
            return str_r[index],counter
        counter = counter+1



print(first_non_repeating("CODE2HELL"))
