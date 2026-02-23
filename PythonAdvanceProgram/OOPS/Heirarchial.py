#Heirarchial Inherita

class Employee:

    def login(self):
        print("emp is logged in")

class Developer(Employee):

    def write_code(self):
        print("writting code")

class Tester(Employee):

    def testing(self):
        print("Testing the app")


dev = Developer()#child 1
test = Tester()#child 2

dev.login()
dev.write_code()

test.login()
test.testing()
