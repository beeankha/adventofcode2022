# Read file, append each entry into a list
f = open("day4_input.txt", "r")
input_list = []
for i in f.read().split("\n"):
    if not i:
        continue
    for x in i.split(",\n"):
        if not x:
            continue
    input_list.append(x)

# Separate each bit out into their own lists

top_range_value_1 = [item.split('-')[0] for item in input_list]
top_range_value_holding_zone = [item.split('-')[1] for item in input_list]
top_range_value_2 = [item.split(',')[0] for item in top_range_value_holding_zone]
bottom_range_value_1 = [item.split(',')[1] for item in top_range_value_holding_zone]
bottom_range_value_2 = [item.split('-')[2] for item in input_list]

# Check if starting/ending numbers of the ranges are within the corresponding range (top vs bottom, bottom vs top)
# If a range is contained within the other, then add a +1 counter to overlap total

counter_list = []

def find_contained_range(top1, top2, bottom1, bottom2):
    if int(top1) >= int(bottom1) and int(top2) <= int(bottom2):
        counter_list.append(1)
    elif int(top1) <= int(bottom1) and int(top2) >= int(bottom2):
        counter_list.append(1)
    else:
        counter_list.append(0)
    return counter_list

while len(top_range_value_1) > 0:
    a = top_range_value_1[0]
    b = top_range_value_2[0]
    c = bottom_range_value_1[0]
    d = bottom_range_value_2[0]
    x = find_contained_range(a, b, c, d)
    top_range_value_1.remove(a)
    top_range_value_2.remove(b)
    bottom_range_value_1.remove(c)
    bottom_range_value_2.remove(d)

# Print the overlap total
print(sum(counter_list))
