#operator polymorphism means same operator behaves differently
# + add nums
# + joins the strings
# + merge the list
# operator overloading in pthon
#methods are--- __adds__()
# __sub__()
# __mul__()
# __eq__()

class Num:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Num(10)
n2 = Num(15)
print(n1+n2)


# now + will work for the custom object
# subtraction
class Num:
    def __init__(self,value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

n1 = Num(100)
n2 = Num(15)
print(n1-n2)



#multiply
class Num:
    def __init__(self,value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value

n1 = Num(10)
n2 = Num(15)
print(n1*n2)

# greater than
class Num:
    def __init__(self,value):
        self.value = value

    def __gt__(self, other):
        return self if self.value > other.value else other

n1 = Num(10)
n2 = Num(15)
print((n1>n2).value)

# lesser than
class Num:
    def __init__(self,value):
        self.value = value

    def __lt__(self, other):
        return self if self.value < other.value else other

n1 = Num(10)
n2 = Num(15)
print((n1<n2).value)

# equals to
class Num:
    def __init__(self,value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

n1 = Num(10)
n2 = Num(10)
print(n1==n2)



