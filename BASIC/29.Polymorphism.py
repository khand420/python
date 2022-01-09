# What is Polymorphism?
# Polymorphism in Python
# Polymorphism with Function and Objects
# Polymorphism with Class Methods
# Polymorphism with Inheritance


# 1.Polymorphism is taken from the Greek words Poly (many) and morphism (forms). It means that the same function name can be used for different types. This makes programming more intuitive and easier.


# 2.Polymorphism in Python
# A child class inherits all the methods from the parent class. However, in some situations, the method inherited from the parent class doesn’t quite fit into the child class. In such cases, you will have to re-implement method in the child class.


# 3.Polymorphism with Function and Objects
class Tomato():
    def type(self):
        print("Vegetable")
    def color(self):
        print("Red")

class Apple():
    def type(self):
        print("Fruit")
    def color(self):
        print("Yellow")


def func(obj):
    obj.type()
    obj.color() 


obj_tomato = Tomato()
obj_apple = Apple()
func(obj_tomato) 
func(obj_apple)  




# 4.Polymorphism with Class Methods
class India():
     def capital(self):
       print("New Delhi")
 
     def language(self):
       print("Hindi and English")
 
class USA():
     def capital(self):
       print("Washington, D.C.")
 
     def language(self):
       print("English")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()



# 5.Polymorphism with Inheritance 
class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()
   
