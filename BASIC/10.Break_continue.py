    # BREAK STATEMENT
    # "break" says "I'm done with this loop entirely." For example, you might want to loop through the customers until you find the one you're looking for. Once you've found it, you don't need to keep looking at other customers, so kick out of the loop.

# 1.1 forloop number data-type
for i in range(0, 5):
    if(i == 4):
        break
    print(i)
else:
    print("Run into esle Block")
print("The end")    


# 1.2 whileloop numbers data-type
i = 0
while(i<=4):
    i = i+1
    if(i == 4):
        break
    print(i)
else:
    print("Run into esle Block")
print("The end")       



# 1.3for String data-type
for val in "string":
    if(val == "n"):
        break
    print(val)
else:
    print("Run into esle Block")
print("The end") 


# CONTINUE STATEMENT
# "continue" says "I'm done with this iteration of the loop. Go on to the next one." For example, you might be looping through a set of customers and you find one with no orders. You don't need to keep going with the part of your loop that has to do with orders, so you say "continue".

# 2.1.continue statement number data-type
for i in range(0, 5):
    if(i == 4):
        continue
    print(i)
else:
    print("Ran into esle Block")
print("The end")  


# 2.2for String data-type
for val in "string":
    if(val == "n"):
        continue
    print(val)
else:
    print("Run into esle Block")
print("The end")


# 2.3whileloop numbers data-type
i = 0
while(i<=4):
    i = i+1
    if(i == 4):
        continue 
    print(i)
else:
    print("Run into esle Block")
print("The end")   