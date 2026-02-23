#exceptions -- runtime errors which will disrupt the normal program flow
#benifits
# helps in debugging
#prevents program crashing
#hadling errors and exceptions in the code more efficiently

# try except
# try - code to be executed
#except - exceptions details catching
# else - if the exception does not occur then else part will get executed
# finally - mandated code

#custom exception

try:
    a = int(input("enter the num"))
    b = int(input("enter the num2"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide a num by zero")
except ValueError:
    print("enter valid num")

# generic exception

try:
    a=5/0
except Exception as e:
    print(e)

#runs if no exception occurs
else:
    print("division successfull")

#mandator codes
finally:
    print("exit the browser")


#custom exceptions - create own exception

age = int(input("enter the age"))
if age < 18:
    raise ValueError("Age must >18")


# que-- 2.write a program to handle invalid user input

try:
    a = int(input("enter the num"))
    b = int(input("enter the num2"))
    sum=a+b
    print(sum)
except ValueError:
    print("enter valid num")



# que-- 3.Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

