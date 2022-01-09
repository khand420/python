

def evaluteExpression(arr):
    stack = []
    operators = ["+","-","*","/","%"]

    for item in arr:
        if item not in operators:
            stack.append((item))
        else:
            first = int(stack.pop())
            second = int(stack.pop())

            if(item == "+"):
                stack.append(second + first)

            if(item == "-"):
                stack.append(second - first)

            if(item == "*"):
                stack.append(second * first)

            if(item == "/"):
                stack.append(second / first)

            if(item == "%"):
                stack.append(second % first)

    return stack[-1]

A = ["2","1","+","3","*"]

print(evaluteExpression(A))

