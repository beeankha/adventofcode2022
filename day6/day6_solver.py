# Read the input from file
f = open("day6_input.txt", "r")
transmission_code = []

for a in f.readlines():
    for i in a:
        transmission_code.append((i))

# Take chunks of n letters and determine if they are unique (but not if it's the first n letters)
# Print index at which the previous n characters are unique, then break

holding_zone = []
index_1 = 0
index_2 = 4  # for part 2 just change this value to 14

while index_2 <= len(transmission_code):
    holding_zone = transmission_code[index_1:index_2]
    print(holding_zone)
    if holding_zone != set(holding_zone):
        index_1 += 1
        holding_zone.pop(0)
        holding_zone.append(transmission_code[index_2])
        index_2 += 1
    if(len(set(holding_zone)) == len(holding_zone)):
        print("unique!")
        print(index_2)
        break
