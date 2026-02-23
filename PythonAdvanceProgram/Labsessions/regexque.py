# Write a regex to check if a string contains only digits.
import re

text = "123456"
result = re.fullmatch(r"\d+", text)
print(result is not None)

# Write a pattern to match a 10-digit mobile number.

number = "9876543210"
print(re.fullmatch(r"\d{10}", number))
# Find all lowercase letters in a string.

text = "Hello World"
print(re.findall(r"[a-z]", text))

# Extract all uppercase letters from a sentence.
text = "Hello World PYTHON"
print(re.findall(r"[A-Z]", text))

# Match a string that starts with "Hello".
text = "Hello everyone"
print(re.match(r"^Hello", text))

# Match a string that ends with "world".
text = "Hello world"
print(re.search(r"world$", text))

# Find all words separated by spaces.
text = "Python is very powerful"
print(re.findall(r"\w+", text))

# Match exactly 5 characters.

text = "Hello"
print(re.fullmatch(r".{5}", text))

# Find all occurrences of the word "python" (case-sensitive).

text = "python is fun. python is easy."
print(re.findall(r"python", text))

# Replace all spaces in a string with underscores.

text = "Hello World Python"
new_text = re.sub(r"\s", "_", text)
print(new_text)

