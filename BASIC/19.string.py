# String is a group of character
# it is immutable





print('''String is a group of character. String follow both forwar and backword indexing.
string is also a data built in data type in python.
''')


str1 = "String is immutable"
# indexing value 
# print(str1[6])
# print(str1[2:5])
# print(str1[::2])



# ------Built in method String----------

#1. strip()  rstrip() lstrip()
s= "    he   llo  worl     d    "
x1 = s.strip()                           #remove all white spaces from left right
# print(x1)

str2 = ",,,,hell...0,,,,w---o..rl...  d"
x = str2.rstrip(",.- ")
# print(x)

low = str1.lower()                      #convert into lower case
# print(low)
low = str1.upper()                      #convert into upper case
# print(low)




#2 Concatenate
# print(str1 +" OR "+s)
# print(str1 * 3)

# iteration 
# for element in str1:
    # print(element, end=' ')




#3 find() or Index() method

str3 =  "String is a group of character. it is immutable"
f=str3.find("is",11)
# print(f)

ind = str3.index("of")   
# print(ind)




#4 replace() method
# string.replace(oldvalue, newvalue, count)

repl = str3.replace("character", "word")
# repl = str3.replace("character", "word",3)
# print(repl)




#5 split() method
# string.split(separator, max)
# 1.default seperator is any whitespace
# 2.when max is specified, the list will contain the specified number of elements plus on. Optional.Specifies how many split to do. Default value is -1.

splt = str3.split()
# splt = str3.split(", ")
# print(splt)

str4 = "kk@ink@kljr@orjoj@scla"
sep = str4.split("@")             #seprate all the stationary iteme in the form of list
sep = str4.split("@",2)
print(sep)





# 6. ord(), chr()
# ord() function return the number repersenting the unicode code of a specified character
# Syntax:
# ord(character)

print(ord('A')) # unicode no = 65
print(ord('a'))  # unicode no = 97
print(ord('😀'))  # unicode no = 128512
smily = ['😀','😁','😂','😃','😄','😅','😆','😇','😈','😉','😊','😋','😌']
for i in smily:
    print(ord(i))

# chr() function returns the character that repersents the specified unicode 
print(chr(128512)) 
print(chr(128515))   
for i in range(128512, 128540):
    print(chr(i), end=',')

# replace smily with words
str5 = "We are having good time 😁 in newYork 😚"    
for ch in str5:
    if(ord(ch)>=128510):
        str5 = str5.replace(ch,'Big smily-face')
print(str5)    





# 7.join() is a string method which return a string Concatenated with elements of an iterable 
# Syntax:
# separator.join(Iterable)

list1 = ['daya','harsh','sai','dev'] #change this same as for dict & tuple
separator = '@'
print(separator.join(list1))




# 8. format() method formats the spicified value(s) and insert them inside the string's placeholder{}
# Syntex:
#   string.format(value1, value2...)
# for format string

email_id2 ={"harsh":'harsh@gmail.com', "Dev":'dev@gmail.com', "Uma":'uma@gmail.com', "Nisha":'nisha@gmail.com'}
email2= ' AND '.join("{} sends on email-id {}".format(name, email) for name,email in email_id2.items())
print(email2)


email_id ={"harsh":'harsh@gmail.com', "Dev":'dev@gmail.com', "Uma":'uma@gmail.com', "Nisha":'nisha@gmail.com'}
email= ' AND '.join(f" {name} sends on email-id {email}" for name,email in email_id.items())
# print(email)


email_id3 ={"harsh":'1', "Dev":'2', "Uma":'3', "Nish":'5'}
email3= ' AND '.join(key+'@'+value for key,value in email_id3.items())
# print(email3)




# Q1. AMAZING SUBSTRING
# start with vowels
# abrab--> 7

def amazing_substr(str1):
    vowels = "aeiouAEIOU"
    count = 0
    for i, char in enumerate(str1):
        if char in vowels:
            count+=len(str1)-1
    return count

print(amazing_substr("abrab"))            



