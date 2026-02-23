empty_list=[]
num_list=[1,2,3,4,3]
mixed_list=[1,"str",True,1.21,1]
nested_list=[[1,2],[3,4]]


#accesing the list elements (indexing concept)
print(mixed_list[1])

#modifying the data
mixed_list[4] = 6
print(mixed_list)

#add elements
mixed_list.insert(4,10)#insert at index
print(mixed_list)
mixed_list.append("john")#add at the end
print(mixed_list)

#remove elements

mixed_list.remove("str")
print(mixed_list)

mixed_list.pop()
print(mixed_list)



#list methods

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

print(num_list.count(3))
print(num_list.index(1))
num_list.clear()
print(num_list)

#slicing

#extend list


