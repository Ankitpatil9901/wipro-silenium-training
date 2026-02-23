#class is a template or a blueprint to store the objects
# which describes the state / behaviour of its object
from tkinter.font import names


class Student:
    name= "Amul"
    id=78954

    # self - used to access the attributes of the class defined and it is automatically loaded
    # create a n to access the data
    # self represents the instance of the class

    def displaystuddetails(self):
        print(self.name)
        print(self.id)


# create the object of the class file

a = Student()

a.displaystuddetails()




#-------------------------------------------------------------
#constructors - first





#parameterised constructor

#self.name is a instance variable or a global variable (belongs to the object)
# name is a local variable(exists inside the method)
#if we dont assign it to the self.name the object will not remember the value

# constructor overloading is not supported in python
class Employee:

    def __init__(self, name, salary):
        self.name= name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


e1= Employee("Amit",56632)
e2= Employee("Ankit",156632)

e1.display()
e2.display()



# using * args in constructor
# constructor overloading is supported by args keyword
#we can pass any nums of parameters to the constructor using *args

class Numbers:
    def __init__(self, *args):
        self.value = args

n= Numbers(10,20,30)
print(n.value)

m= Numbers(3,4)
print(m.value)

p= Numbers(4)
print(p.value)


# Parent and child constructors
# super keyword for accessing parent constructor

class Parent:
    def __init__(self):
        print("I am parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am child constructor")

c = Child()



# que Create a class Book with attributes title and author. Create 3 different book objects and print all details.

class Book:
    

# q2 Create a class Book with attributes title and author. Create 3 different book objects and print all details.






#--------------------------------------------------------------

# variables = used to store the data -- class, instance ans local variable
# instance variable - global variables  at class level
# local variable - inside the method only


#instance varriable example

class Student:

    #CLASS VARIABLE
    school="St joseph"
    def __init__(self,name,marks):
        self.name = name # instance or global varriable
        self.marks = marks

    def show(self):
        schoolcity ="FHk" # local variable-scope inside the method
        print(self.marks, self.name)
        print(schoolcity)
        print(self.school)

s1=Student("Amit",89)
s2=Student("Ankit",97)

s1.show()
s2.show()











#class example with 2 objects

class Employee:
    emp_name="Amit"
    emp_id = 111
    emp_address="Bengaluru"
    emp_dept="it"

    def display_empdetails(self, name, id ):
        print(self.emp_name)
        print(self.emp_id)
        print(self.emp_address)
        print(self.emp_dept)












