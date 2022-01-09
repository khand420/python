def anagram(A):
    if(A==None):
        return
    else:
        dict = {}
        for i in range(len(A)):
            word = ''.join(sorted(A[i]))
            print(word)
            if(word not in dict):
                dict[word] = [i+1]
            else:
                dict[word].append(i+1)
        return dict

A = ["cat", "dog", "god", "tca","act"]
print(anagram(A))                    

