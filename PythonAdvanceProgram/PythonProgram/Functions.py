#zFunction is a block of code that performs specific task
# def functionname
from PythonProgram.iterator import value


#default function with no parameters
def printdata():
    print("Hello")

#call the function
printdata()

#function with parameters

def printdata(name):
    print("Hello",name)

#pass the argument
printdata("amit")
printdata("amul")



def sq(num):
    res=num*num
    return res

sqs=sq(3)
print(sqs)

#funtion pass

def fun_pass():
    pass

fun_pass()

#multiple return values

def call(a,b):
    return a+b, a-b,a*b

add, sub , mul = call(10,5)
print(add)
print(sub)
print(mul)


def areaofrect(len, width):
    return len * width

def areaofsq(side):
    return side * side

val = areaofrect(4,5)
sq = areaofsq(val)
print(sq)


def even(limit):
    if limit %2==0:
        return "even"
    else:
        return "odd"

print(even(10))
print(even(11))






