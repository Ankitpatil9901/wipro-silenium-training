class A:

    def show(self):
        print("Class A")

class B(A):
    #def show(self):
        pass
        #print("class B")

class C(A):
    pass
    #def show(self):
     #   print("class C")

class D(B,C):
    pass
    #print("class d")


d = D()
d.show()
print(D.mro())

# methods from left to right   output seq is d--b--c--a


#diamond with super key word


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("class B")

class C(A):
     def show(self):
         super().show()
         print("class C")

class D(B,C):
    def show(self):
        super().show()
        print("class d")


d = D()
d.show()
print(D.mro())






