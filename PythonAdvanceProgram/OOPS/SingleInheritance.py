# single inheritance
# parent -- child class - properties from parent class are acquired to child class
from mimetypes import add_type


# parent class

class Employee:
    def __init__(self,name, empid):
        self.name =name
        self.empid = empid

    def empdetails(self):
        print(self.name, self.empid )

class Manager(Employee):

    def approve_leave(self):
        print("leave approved")

m = Manager("Amit", 158)
m.empdetails()# from parent class

m.approve_leave() # from child class


# create a python program with class name savingsccount and functions deposit in parent class  and  addinterest in the child class


class Sanvigsaccount():

    def __init__(self,bal=0):
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount
        print(f"Amount deposited - {amount}")
        print(f"Bal is {self.bal}")


class addInterest(Sanvigsaccount):
    def addInterest(self, intrate):
        Int = (self.bal*intrate)/100
        self.bal += Int
        print(f"{self.bal}")
        print(f"{Int}")

a=addInterest()

a.deposit(1000)
a.addInterest(3)
