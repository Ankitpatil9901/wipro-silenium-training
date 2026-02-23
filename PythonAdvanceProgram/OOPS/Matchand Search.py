# match = match the exact seq

import re

# output is match object - matched sequence and span() - start and end index

text = "hello"
result= re.match("hello", text)
print(result)

# using pattern

test = "5427891arfeuGFRIUHJK"
pattern = re.compile("arf")

#re.findtter finds all non overlapping matches of a pattern in a string and returns an terator of match object not a list
matches = pattern.finditer(test)



for match in matches:
    print(match)
    print(match.group())
    print(match.span())


# search operation search the entire string
# returns onl the 1st occurance

txt = "java is a powerfull lang"
res = re.search("powerfull", text)
print(res)
# modification methods
# search -- search the entire string -- find the occurances and returns onl 1st occurance
# match -- beggining only  - validate the format

# raw string  - for  including the special character

a = r"\tHello"
print(a)

# findall()- find all the strings where the re matches and return a list

mystr = "adfghjk78212352123"
pattern = re.compile(r"123")
matches = pattern.findall(mystr)

for match in matches:
    print(match)

# Methods on match.

# group() - Return the string method by the re
# start() - return the starting position of the match
 # end() - return the ending position of the match
# span() - return thetuple containing the (start, end) position of the match

test =  "adfghjk78212352123"
pattern = re.compile(r'adf')
matches = pattern.finditer(test)

for match in matches:
    print(match)
    print(match.span(), match.start() ,match.end())
    print(match.group())


# special characters
# meta characters
# regular expressions

# Pattern Meaning
# abc Matches exact text
# [abc] a or b or c
# [a-z] lowercase letters
# [0-9] digits

# abc Matches exact text
text = " I like abc and abcde124785"
result = re.findall("[a-z]", text)
print(result)
# 0-9
text = " I like abc and abcde124785"
result = re.findall("[0-9]", text)
print(result)
# 'a b'
text = " I like abc and abcde124785"
result = re.findall("cat | bat", text)
print(result)



# special char

#\S Non whitespaces \S - Matches anything that is NOT space,tab,newline.
text = "hi there"
result = re.findall(r"\S",text)
print(result)

# \b Word boundary → Matches position at start or end of a word.
text = "cat scatter catalog"
result = re.findall(pattern=r"\bcat\b", string=text)
print(result)

# Matches only full word "cat"

# \B Not a word boundary → Matches when pattern is NOT at word boundary.
text = "cat scatter catalog"
result = re.findall(pattern=r"cat\B", string=text)
print(result)




