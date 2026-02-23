# lambda fun - anonymous (nameless) fun, one line, simple operations
# syntax lambda arguments : expression
# filter alwas return true values

#it can have any num of arguments
# must have only one expression
# expression is automatically returned

#map always give true or false and it applied on all values


# fun - fun name, arguments, return tpe, code


# normal func for adding 2 num

def add(a,b):
    return a+b
print(add(5,6))

#lambda function
add = lambda a,b: a+b
print(add(5,9))

# square of a num using lambda

sq = lambda a: a*a
print(sq(5))

#check even or odd
ev = lambda a: a%2==0
print(ev(6))

#find max of 2 num

max= lambda a,b: a if a>b else b
print(max(5,9))

# inbuilt function - filter map and reduce
# filter - select data/ filtering
#map- transform the data
# reduce - aggregate the data

#filter

num = [1,2,3,4,5,6]
even = list(filter(lambda a: a%2 == 0, num))
print(even)


# filter the failed status

status =['Pass','Fail','Pass','Fail']

failed =list(filter(lambda s:s == 'Fail', status))
print(failed)


#filter + ve numbers
nums = [-5, 10, -3, 7, 0, 2]
pos=list(filter(lambda s:s >0 , nums))
print(pos)


 #Filter non-empty strings

data = ["hello", "", "world", "", "python"]
emp=list(filter(lambda s:s == '', data))
print(emp)




#reduce - aggregate - combining many values to a single unit

from functools import reduce
nums = [10,20,30,40]
print(reduce(lambda x,y : x+y, nums))

#multiply, max val, min value

print(reduce(lambda x,y:x*y, nums))

print(reduce(lambda x,y: x if x>y else y,nums))

print(reduce(lambda x,y: x if x<y else y,nums))




#map - transform the data- the function is applied to every element

nums =[10,20,30,40]

squares = list(map(lambda x: x*x, nums))
print(squares)


# sorting in lambda
data = [(1,3), (4,1), (2,2)]
sort=sorted(data, key= lambda x:x[1])
print(sort)

marks={"A": 75, "B":90, "C":80}
sort1= dict(sorted(marks.items(), key=lambda x:x[1]))
print(sort1)