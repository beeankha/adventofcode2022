import string

# Read file, append each entry into a list
f = open("day3_input.txt", "r")
input_list = []
for i in f.read().split("\n"):
    if not i:
        continue
    input_list.append(i)

# Find the duplicate value in each 3 string group
duplicate_values = []

def find_dup(str1, str2, str3):
    return [i for i in set(str1) if i in set(str2) and i in set(str3)]

while len(input_list) > 0:
    a = input_list[0]
    b = input_list[1]
    c = input_list[2]
    x = find_dup(a, b, c)
    input_list.remove(a)
    input_list.remove(b)
    input_list.remove(c)
    duplicate_values.append(x[0])

# Assign values to each letter (lower and uppercase)
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27

# Convert each repeating character into int values and then sum the total
values_list = []
for duplicate_char in duplicate_values:
    number = values[duplicate_char]
    values_list.append(number)

print(sum(values_list))
