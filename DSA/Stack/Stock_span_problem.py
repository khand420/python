


def calculateSpan(price, span):
    n = len(price)
    stack = []
    stack.append(0)
    span[0] = 1
    

    for i in range(1, n):
        while(len(stack) > 0 and price[stack[-1]] <= price[i]):
            stack.pop()
        if len(stack) <= 0:
            span[i] = i + 1 

        else:
            span[i] = (i - stack[-1])
        stack.append(i)
    return span           

price = [60, 70, 80, 100, 90, 75, 80, 100]
span = [0 for i in range(len(price))] 

print(calculateSpan(price, span))