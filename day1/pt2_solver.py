# Read input file
f = open("pt1_input.txt", "r")
input_list = []
for i in f.read().split("\n\n"):
    sublist = []
    if not i:
        continue
    for x in i.split("\n"):
        if not x:
            continue
        sublist.append(int(x))
    input_list.append(sublist)

new_list = []
for sub_list in input_list:
   new_list.append(sum(sub_list))

new_list.sort()

# calculate the top 3 elfsnacks
first = new_list[-1]
second = new_list[-2]
third = new_list[-3]
total = first + second + third

print(total)
