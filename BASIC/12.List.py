# LIST = Heterogenous Elements(mixed type of values)
# *Zero Based Indexing
# *Duplicates allowed
# *Mutable
# *Variable Length

# for example 
# list = [22, 43.2, 5, "isYou",'d',5, 3.222]




# ******APPEND*********
# a1 = [1,2,4,9]

# a1.append([19,3,'flag'])
# print(a1)
# print(type(a1))
# print(type(a1[0]))
# print(type(a1[4][2]))

# # 1.Indexing-Accessing element from list 
# print(a1[-1])
# print(a1[-2])
# print(a1[-3])

# # 1.2length of list 
# print(len(a1))


# ******EXTEND*********
# a2 = [5, 6, 9, 3]

# a2.extend([19,3,'flag'])
# print(a2)

# a3 = ['a', 'b', 'new', 'migrations', 'z', 'example', 'new',['new',2]]
# a3.extend(["two", "elements"])
# print(a3)

# print(type(a3[0]))
# print(type(a3[7]))
# print(type(a3[7][0]))

# str = ["neena", "meena"]
# print(a2 + str)


# ******INSERT*********
digit = ['a', 'b', 'new', 'migrations', 'z', 'example']
digit.insert(2, "new")
print(digit)



# ******DEL REMOVE*********

#del removes the item at specicfic index
b= [3,2,2,1]
del b[1]
print(b)

#pop removes the item at a specific index and returns it
a = [4, 3, 5]
c = a.pop(1)
print(c)
print(a)

# removes the first matching value in given list
d = [0, 2, 3, 2]
d.remove(2)
print(d)


# REVERSE 
# Inputlist = [10, 11, 12, 14, 15]
# Inputlist.reverse()
# print(Inputlist)


# **********list SORITING**********
# SORT 
# s = [1, 7, 4, 6]
# s.sort()
# # s.sort(reverse=True) 
# print(s)

# SORTED 
# s1 = [1, 7, 4, 6]
# s2= sorted(s1) #return the new list
# print(s2)

# SORT BY LENGHT
# s = ['ccc', 'aaa', 'd', 'bb']
# d = sorted(s, key=len)
# print(d)

# note 
# l = [10, 20, 30]
# m = l
# m.append(40)
# print(m)
# print(l)


# ********SPLIT ********
# split a string into a list 
# txt = "welcome,2,code2hell,for,coding"
# x = txt.split(',')

# txt = "we lcome 2 code2hell for coding"
# x = txt.split(' ')
# print(x)


# ********SLICING********
# slice[start:end:stepsize]
name=['Reena', 'Sheena', 'Meena', 'Teena', 'Neena', 'Leena']
print(name[:])
print(name[:3])

print(name[::2])
print(name[2::2])



# ********COUNT********
num = [1,5,1,4,6,3,1,4,6,6]
print(num.count(6))

