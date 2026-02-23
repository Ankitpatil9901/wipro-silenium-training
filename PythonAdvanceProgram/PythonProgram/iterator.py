#iter() method - built in method
#iterations - looping in the collection of items


#convert the dict into iterator

d={'a':1,'b':2,'c':3}
iterator = iter(d)
print(next(iterator))



#for loop to iterator

d={'a':1,'b':2,'c':3}
iterator = iter(d)

print(next(iterator))
#for loop iterate
for key in iterator:
    print(key)


d={'a':1,'b':2,'c':3}
for key,value in d.items():
    print(key,"-",value)

# iter(callable, sentinal)

it = iter(input, "quit")

for value in it:
    print(value)

def get_input():
    return input("enter Value")

for value in iter(get_input, "quit"):
    print("you entered",value)

print("loop ended")


#Create a custom iterator that prints numbers from 1 to 5.
#Write an iterator class that returns next even number.
#Explain and demonstrate the use of __iter__() and __next__().