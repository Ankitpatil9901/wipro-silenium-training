
class Employee:
    def __init__(self,name, empid):
        self.name =name
        self.empid = empid

    def empdetails(self):
        print(self.name, self.empid )

class Manager(Employee):

    def approve_leave(self):
        print("leave approved")

class SrManager(Manager):
    def approve_budget(self):
        print("Budget Approved")

sm = SrManager("Amit", 158)
sm.empdetails()# from parent class

sm.approve_leave() # from child class
sm.approve_budget()