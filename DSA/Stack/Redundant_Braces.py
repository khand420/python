def redundant_braces(N):
    stack = []
    for i in range(len(N)):
        if(N[i] in '(+-*/' ):
            stack.append(N[i])

        elif(N[i]== ')'):
            if( stack.pop()=='(' ):
                return 1
            stack.pop()
    return 0


# N = "((a+b))"
N = "((a+b)*c)"

a = redundant_braces(N)
if(a == 1):
      print("Redundant")
else:
    print("Not a Reduntant")               

     