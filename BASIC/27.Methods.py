# There are three types of methods in Python:

# Instance Methods.

# Class Methods

# Static Methods


# Before moving on with the topic, we have to know some key concepts.

# Class Variable: A class variable is nothing but a variable that is defined outside the constructor. A class variable is also called as a static variable.

# Accessor(Getters): If you want to fetch the value from an instance variable we call them accessors.

# Mutator(Setters): If you want to modify the value we call them mutators.


# self vs cls
# The difference between the keywords self and cls reside only in the method type. If the created method is an instance method then the reserved word self has to be used, but if the method is a class method then the keyword cls must be used. Finally, if the method is a static method then none of those words will be used because as said before, static methods are self-contained and do not have access to the instance or class variables nor to the instance or class methods.


# Instance Method Example in Python 
class Student:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    def avg(self):
        return (self.a + self.b) / 2

s1 = Student(10, 20)
print( s1.avg() )



# Class Method Implementation in python 
class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @classmethod
    def info(cls):
        return cls.name

print(Student.info())



# Static Method Implementation in python
class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @staticmethod
    def info():
        return "This is a student class"

print(Student.info())






# class MethodTypes:

#     name = "Ragnar"

#     def instanceMethod(self):
#         # Creates an instance atribute through keyword self
#         self.lastname = "Lothbrock"
#         print(self.name)
#         print(self.lastname)

#     @classmethod
#     def classMethod(cls):
#         # Access a class atribute through keyword cls
#         cls.name = "Lagertha"
#         print(cls.name)

#     @staticmethod
#     def staticMethod():
#         print("This is a static method")

# # Creates an instance of the class
# m = MethodTypes()
# # Calls instance method
# m.instanceMethod()


# MethodTypes.classMethod()
# MethodTypes.staticMethod()