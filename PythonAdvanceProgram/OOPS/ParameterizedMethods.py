# default method - builtin methods , user defined methods- method name method body
# parameterized method (multiple parameters)

class Calculator:

    def add(self,a,g):
        print(a+g)

c = Calculator()
c.add(10,8)
c.add(8,9)


# default parameters
class Test:
    def run(self, browser = "chrome"):
        print("Running on",browser)

t = Test()
t.run()
t.run("Firefox")

# * args parameterized methods

class Nums:
    def total(self,*args):
        print(sum(args))

n = Nums()
n.total(10,50,70)
n.total(10,8)
n.total(80)






