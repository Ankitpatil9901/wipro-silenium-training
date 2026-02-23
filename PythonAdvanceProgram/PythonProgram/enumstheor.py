# enumerate with list
fruits = ["Apple","Kiwi","Orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


#enumerate start value change

for index, fruit in enumerate(fruits , start=1):
    print(index, fruit)

# enumerate with string

word = "Java"

for index,ch in enumerate(word, start =2):
    print(index,ch)

# enumerate with tuple
fruits = ("Apple","Kiwi","Orange")

for index, fruit in enumerate(fruits):
    print(index, fruit)

# real time scenerio

test_cases =["login", "Signup" , "checkout"]
for case_no,test in enumerate(test_cases):
    print(f"executing Testcases {case_no}: {test}")

# accessing of theb enumerate values

a = ['God', 'is', 'Great']
b = enumerate(a)
nxt_val = next(b)
nxt_val = next(b)
nxt2_val = next(b)
print(nxt_val)
print(nxt2_val)
# duplicate detection using enumeration

characters = ["kalu", "Goku", "Gohan", "Goku"]
character_map = {character: [] for character in set(characters)}

for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map )