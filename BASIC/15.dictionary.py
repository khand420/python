# Dictionary - Python is  an un-ordered collection of data values, used to store data values like map, 
#             which unlike other Data Type that only single as an element, Dictionary holds key:value pair.

# *key will be a single element
# *values can be a list or list whithin a list, number, etc.


        # PROPERTIES   
# *No duplicate key is allowed
# *The values in the dictionary can be of any type while the keys must be immutable like number, tuple or string.
# *Dictionary keys are case sensitive-Same key name but  with the different case are treated as different keys in Python dictionaries.   
        

       # TIME COMPLEXITY
    #  LIST, TUPLE =     O(n)
    #  DICTIONAY, SET =  O(1)


empyt_dict = {}           #empty dictionay
print(type(empyt_dict))


# ways to define dictionary

a= {}
a['jan'] = 1
a['feb'] = 2
a['mar'] = 3

print(a)

dict1 = {1: 'code', 2: 'two', 3: 'hell'}  #dictionay of integer
print(dict1)

dict2 = {'Name':'Danish', 1:[1,2,3,4]}    #dictionary of mixed value
# print(dict2)
print(dict2.values())
print(dict2.keys())
print(dict2['Name'])
# print(dict2['name'])                        # *Dictionary keys are case sensitive-Same key name but  with the different case are treated as different keys in Python dictionaries.   
# print(dict2['age'])  
    #    or
print(dict2.get('Name')) 
print(dict2.get(1)) 


dict3 = dict([(1, 'python'), (2, 'java')])  #dictionary of list of tuple
print(dict3)


# ************DICTIONARY OPERATIONS************
a = {1: 'jan', 2:'feb', 3:'mar', 4:'apr', 5:'may'}
# b = dict(a)
#  or
b = a.copy()
# print(b)

dict1 ={'Name': 'Rahul', 'Class':5, 'Roll No':34}     #update value
dict1['Name'] = 'Anjali'
# print(dict1)

dict1['Address'] = 'Wassepur, Dhanbad'        #add new key
print(dict1)

dict2 = {'Name': 'Anjali', 'Class': 5, 'Roll No': 34, 'Address': 'Wassepur,Dhanbad'}
del dict2['Address']                          #del method - didn't return value
# print(dict2)

# c = dict2.pop('Roll NO')
# print(dict2)                                  #pop method - return the value

d = dict1.popitem()                             #return the value
print(d)

dict2.clear()                                   #clear value
print(dict2)

# del dict1
# print(dict1)




# NOTE:- keys are must be immutable. example give below

# t_dict = {'name': 'john', 1:[2,4,3], ('age',3):34}    #tuple inside dictionary
# print(t_dict)

# l_dict = {'name': 'john', 1:[2,4,3], ['age',3]:34}   #list inside dictionary
# print(l_dict)

# d_dict = {'name': 'john', 1:[2,4,3], {'age',3}:34}   #dictionary inside dictionary
# print(d_dict)


# *********fromekeys()********** 

# dict.fromkeys(iterable, Values)
# 1.list
# 2.tuple
# 3.range
# 4.dictionary 


listd = [10,20,30,40,50,60]
dictl ={}.fromkeys(listd, 0)    #list is iterable
print(dictl)

# inte  = 4
# dicti = {}.fromkeys(inte, 0)    #integers are not iterable
# print(dicti)

tup1 = (4,3)
dictt= {}.fromkeys(tup1, 0)      #tuple is iterable
print(dictt)

dictd = {1: 'name', 2: 'age'}    #dictionary is iterable
dict8 = {}.fromkeys(dictd, 0)

a = range(0,5)
dictr = {}.fromkeys(a,0)        #range is iterable
print(dictr)

# listdm = [10,20,[30,40,50,60]]
# dictl ={}.fromkeys(listdm, 0)    #list is mutable inside key
# print(dictl) 

# tup1i = [1,2,3(4,5,6)]
# dictti= {}.fromkeys(tup1i, 0)      #tup1i is iterable because tuple immutable
# print(dictti)



# *********setDefault()********** 
# it always insert the key in a original dictionary
# dict.setdefault(key, Values)

Sdict = {'a':1,'b':2,'c':3,'d': 4}
print(Sdict.setdefault('e',5))
print(Sdict)

car = {"brand":"food", "model": "Mustang","year":1999}
print(car.get("color"))
if(car.get("color")==None):
    car["color"] = "white"  
print(car)

car = {"brand":"food", "model":"Mustang", "year":1999}
print(car.setdefault("color", "RED"))
print(car)



# ************len,item(),keys(),values(),Membership() Operator, Method in Dictionary************** 

a = {'apple':'fruit','beetroot':'vegetable','doughnut':'snack'}
print(len(a))                                                               #Length of dictionary

member = {1:1,2:4,3:9,4:16,5:25}
print (25 not in member)                                                    #Membereship check key return T/F
print (5 in member)  

print(member.items())                                                     #Shows all item in dictionary in the form of tuple

print(member.keys())                                                       #Shows all key present in dictionary
print(member.values())                                                     #Shows all value present in dictionary

for i in member:
    print(member[i])                                                       #print dict value in iterated way

for j in member.items():                                                    #all the key&value as tuple in iterated way
    print(j)   



# UPDATE 
dict1 ={'Name': 'Rahul', 'Class':5, 'Roll No':34}     #update value
dict1['Name'] = 'Anjali'
# print(dict1)

d2 ={'Name': 'Rahul', 'Class':5, 'Roll No':34}     #update() in tuple
t2 = (('Name','Amit'),('Class',1))
d2.update(t2)
print(d2)

# d3 ={'Name': 'Rahul', 'Class':5, 'Roll No':34}     #update() in list
# l2 = ['Roll No', 420]
# d3.update[l2]
# print(d3)