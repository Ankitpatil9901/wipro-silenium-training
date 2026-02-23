# descriptors - used for control the access of the object attributes
from tkinter.font import names


# _get_()
# _set_()
# _delete_()

class Desc:
    def __get__(self, instance, owner):
        print("getting the value")
        return 10

class Test:
    x = Desc()

t= Test()
print(t.x)

# this is non - data descriptor - it uses only get descriptor
# data descriptor - it uses set and  get descriptor

class mydesc:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, owner):
        print("setting the value")
        instance._value = value



t = Test()
t.x = 100
print(t.x)

class Name:
    def __get__(self, instance, owner):
        return instance._name


    def __set__(self, instance, value):
        print("setting the value")
        instance._name = value

    def __delete__(self, instance):
        print("deleting the name")
        del instance._name

class Person():
    name =Name()

p = Person()
p.name = "Ankit"
del p.name







