
def wordBreak(word, dict):
    m=len(word)
    T= [[False for x in range(m)] for y in range(m)]

    for l in range(1,m+1):
        for i in range(0,m-l+1):
            j = i + l-1
            str = word[i:j+1]
            if str in dict:
                T[i][j] = True
                continue

            for k in range(i+1, j+1):
                if(T[i][k - 1] != False and T[k][j] != False):
                    T[i][j] = True
                    break
    
    if T[0][m-1] == False:
        return False
    else:
        return True

dict1=['i', 'am', 'nun']
str1 = "iamnun"
print(wordBreak(str1,dict1))   


                
