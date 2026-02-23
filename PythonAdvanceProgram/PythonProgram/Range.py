#all nos shld integers
# step size cannot 0

#range does not creates a list it creates objects
a = range(5)
print(a[1])

# for loop for range of 2 arg
a= range(2,5)
for i in a:
    print(i)

# for loop for range of 3 arg
a= range(2,5,2)
for i in a:
    print(i)

# for loop for range of negative 3 arg
a= range(2,5,-3)
for i in a:
    print(i)

# reverse printing
a= range(12,5,-1)
for i in a:
    print(i)

#scenerio Allow login attempts for 3 times
for attempt in range(3):
    pin =input("Enter pin:")
    if pin == "1234":
        print("Access granted ")
        break

    else:
        print("Try again")

#scenerio Allow 3 login 3 times
for attempt in range(3):
    pin =input("Enter pin:")
    if pin == "1234":
        print("Access granted ")
        break

    else:
        print("Try again")