import string

# Read file, append each entry into a list
f = open("day3_input.txt", "r")
input_list = []
for i in f.read().split("\n"):
    if not i:
        continue
    input_list.append(i)

# Take each entry from list and split them exactly in half, and put them in two different lists
first_half_list = []
second_half_list = []
for contents in input_list:
    first_half, second_half = contents[:len(contents)//2], contents[len(contents)//2:]
    first_half_list.append(first_half)
    second_half_list.append(second_half)

# Compare each half-string and figure out which value is repeated (and append those to a new list?)
duplicate_values = []

def find_dup(str1, str2):
    return [i for i in set(str1) if i in set(str2)]

while len(first_half_list) > 0:
    x = find_dup(first_half_list[0], second_half_list[0])
    duplicate_values.append(x[0])
    first_half_list.remove(first_half_list[0])
    second_half_list.remove(second_half_list[0])

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
