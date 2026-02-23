# poly morphism means taking many forms

# same method / fun name will behave differently
# object type
# input arguments
# class implementation

print(len("java"))
print(len([1,2,3]))

class Calci:
    def add(self, a, b=0,c=0):
        return a+b+c

c = Calci()
print(c.add(5))
print(c.add(5,10))
print(c.add(5,9,8))

# runtime polymorphism is supported in python
# achieved through method overriding - child class method will override the parent class method

class Animal:

    def sound(self):
        print("Animal make sound")

class Dog(Animal):

    def sound(self):
        print("dog barks")

a = Dog()
a.sound()







