# A set is an unordered collection of items. Every element is unique(no duplicates). 
# Sets can be perfom mathematical set operations like UNION, INTERSECTION, SYMMETRIC DIFFERENCE etc

# 1.MUTABLE 
# 2.UN-ORDERED - set object doesn't support indexing
# 3.DUPLICATES ARE NOT ALLOWED

emptyset = set()
print(type(emptyset))



# ***********FUNCTIONS*****************

set1 = {'python', 'java', 'c'}  #mutable
set1.add('c++')              # add function use only for adding single item
# print(set1)

set2 = {1,2,3}
set2.update({4,5,6})        # update function use only for adding more than one  item
# print(set2)
# print(set2[0])              # set object doesn't support indexing


# set from a list 
a = set([10, 34, 53, 52, 21])
print(a)

# list with set 
list1 = [1,2,3]
list2 = [5,6,7]
list3 = [10,11,12]

set1 = set(list2)
set2 = set(list1)
set1.update(set2)
print(set1)

set1.update(list3)
print(set1)


# remove pop clear discard
a = {1,4,5,6,8}
a.remove(1)
# print(a)
a.discard(8)
# print(a)

b= {"java", "python", "c++"}
# b.remove("html")
b.discard("html")
# print(b)

s = {1,3,4,6,0,9}
c = s.pop()              #remove random element
# print(s)

s.clear()                #clear all the element
# print(s)

set3 = {2,3,3,1,4,5,5,6,3,4,7}  #remove duplicates
# print(set3)

a = {10, 20, 30, 40}         #copy elements use the set
b  = set(a)
# print(b)




# ***********OPERATIONS***********

# 1.Union operations
set1 = {2,4,5,6}
set2 = {4, 6, 7, 8}

# 2.print(set1.union(set2))
# print(set1 | set2)


# 3.Intersection operations
# print(set1 & set2)

# 4.set difference
setA = {10, 20, 30, 40, 80}
setB = {100, 30, 80, 40, 60}

print(setA-setB)
print(setB-setA)
print(setA.difference(setB))
 

# 5.Symmetric difference
print(setA.symmetric_difference(setB))
print(setA ^ setB)


#is subset() method returns in Boolean 
# if all item in the set exists in the specified set 

x = {"f", "b", "c"}
y = {"f", "e", "d","c", "b"}

z = x.issubset(y)
print(z)



# **********FROZEN SET*************

# 1.immutable
# 2.can be created using frozenset()
# 3. doesn't support indexing
# 4. Set can't be used as a key in dictionary but frozen set can

nu = (1, 3, 4, 5, 6, 6, 6, 7, 8, 9)
fnum = frozenset(nu)
print(fnum)

se = frozenset([10,30,50,70])
# se.add(90)                       #immutable


student = {"name": "danish", "age": 21, "collage":"bakwas collage of engineering"}
key = frozenset(student)            #frozenset can be used as key in dict
print(key)

subject = ['os', 'dbms', 'algo']
f_subject = frozenset(subject)

# f_subject[1] = 'networking'        #doesn't support indexing