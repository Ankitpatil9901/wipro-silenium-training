#generators - spl type of fun - return onl value at a time on demand
# yield - used only in generators not in normal fun

# memory efficient
# usefull for large set of data
# files, retries, batching

# normal fun - loads all the values into the memory
def num():
    return [1,2,3,4,]

print(num())


#generator fun
def generator():
    print("printing 1")
    yield 1

    print("printing 2")
    yield 2

    print("printing 3")
    yield 3

    print("printing 4")
    yield 4

ret_value = generator()

print(next(ret_value))
print(next(ret_value))

#Write a generator to generate numbers from 1 to N.
#Create a generator to generate even numbers only.
#Write a generator to read a file line by line.
#Create a generator for Fibonacci series.
#Write a generator that simulates retry attempts (max 3 tries).

