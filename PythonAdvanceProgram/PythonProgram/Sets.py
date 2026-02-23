#Sets do not allow duplicate elements it contains only unique data
# unordered collection

Std_id={111,112,113,114,114} #integer type
print(Std_id)

letters = {'a','n','c','d'} #string set
print(letters)

mix_set={1,2,3,'r','t'}
print(mix_set)

emp_set = set()
print(emp_set)

#Set methods
Std_id.add(110)
print(Std_id)

Std_id.discard(111)
print(Std_id)

