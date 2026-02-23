# dictionary items key value pair
# similar to list and tuple
# for integers , tuples, and strings - keys must be immutable
# list cannot be used in the key for dict as it is mutable in nature


country ={
    "India": "delhi",
    "england": "london"
}

print(country)

#access the values with keys
print(country["India"])

#add elements

country["Italy"] = "Rome"
print(country)

#remove elements
del country["england"]
print(country)

# clear

country.clear()
print(country)


#iterate among the dict

for coun in country:
    print(coun)

#length of dict
print(len(country))


# integer as a key

my_dict= {
    1:"one", 2: "two", 3:"three"
}
print(my_dict)

my_dict= {
    1:"four", 2: "two", 3:"three",1:"one"
}
print(my_dict)

#tuple as a key

my_dict={(1,2):"one two", 3:"three"}
print(my_dict)

my_dict={(1,2):"one two", 3:"three", 3:"four"}
print(my_dict)

#list as a key
#my_dict={1:"Hello",[1,2]:"Hi"}
#print(my_dict)


# pop - removes the item with spec key
my_dict1={
    "India": "delhi",
    "england": "london"
}
my_dict1.pop("India")
print(my_dict1)

# update() - adds or changes the dict
my_dict2={
    "India": "delhi",
    "england": "london"
}
my_dict2.update()

#keys()
my_dict2.keys()
# values()
my_dict2.values()

#popitem() return the last inserted key

# copy returns the cop of dict

#dict inside the list

employes= {
    {"id":1, "name":"Amit","role":"erp"},
    {"id":2, "name":"Anil","role":"qa"},
    {"id":3, "name":"Adit","role":"dev"}
}

print(employes[0])

print(employes[0]["name"])

for emp in employes:
    print(emp["name"], emp["role"])


employes.append({"id":4, "name":"Sita", "role":"Tester"})
print(employes)

employes.pop(0)
print(employes)

#search a item in the list

for emp in employes:
    if emp["name"] == "Amit":
        print(emp)