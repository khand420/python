def min_bracket_reversal(exp):
    size = len(exp)
    if size%2 != 0:
        return None

    s = [] 
    for i in range(size):
        if exp[i]=='}' and len(s) > 0:
            if s[0] == '{':
                s.pop(0)
            else:
                s.insert(0,exp[i])

    total_left = len(s)
    open = 0
    while(len(s) >0 and s[0] == '{'):
        s.pop(0)
        open=open+1   
    return total_left//2 + open % 2

expr = "{ { { {"    
print(min_bracket_reversal(expr))                 
