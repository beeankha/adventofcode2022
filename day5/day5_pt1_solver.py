# Read file, append each entry into a list
f = open("day5_input.txt", "r")
number_of_moves = []
origin_stack = []
target_stack = []

for a in f.readlines():
    b = a.split(" ")[1]
    c = a.split(" ")[3]
    d = a.split(" ")[5]
    number_of_moves.append(int(b))
    origin_stack.append(int(c))
    target_stack.append(int(d))

# Create lists of crates

# sample input
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# stack_1 = ['Z', 'N']
# stack_2 = ['M', 'C', 'D']
# stack_3 = ['P']


#non-practice input
# [Q]         [N]             [N]    
# [H]     [B] [D]             [S] [M]
# [C]     [Q] [J]         [V] [Q] [D]
# [T]     [S] [Z] [F]     [J] [J] [W]
# [N] [G] [T] [S] [V]     [B] [C] [C]
# [S] [B] [R] [W] [D] [J] [Q] [R] [Q]
# [V] [D] [W] [G] [P] [W] [N] [T] [S]
# [B] [W] [F] [L] [M] [F] [L] [G] [J]
#  1   2   3   4   5   6   7   8   9 


stack_1 = ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q']
stack_2 = ['W', 'D', 'B', 'G']
stack_3 = ['F', 'W', 'R', 'T', 'S', 'Q', 'B']
stack_4 = ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N']
stack_5 = ['M', 'P', 'D', 'V', 'F']
stack_6 = ['F', 'W', 'J']
stack_7 = ['L', 'N', 'Q', 'B', 'J', 'V']
stack_8 = ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N']
stack_9 = ['J', 'S', 'Q', 'C', 'W', 'D', 'M']

# Create a map for crate stacks via integer

stack_assignment = {
    1: stack_1,
    2: stack_2,
    3: stack_3,
    4: stack_4,
    5: stack_5,
    6: stack_6,
    7: stack_7,
    8: stack_8,
    9: stack_9,
    }

# Take the number in "move" and apply it as an index to target list, move
# that number of items to end of designated crate stack

while len(number_of_moves) > 0:
    move_to_do = int(number_of_moves[0])
    move_index = -abs(move_to_do)

    starting_stack = int(origin_stack[0])
    destination_stack = int(target_stack[0])
    crates_in_trasit = stack_assignment[starting_stack][move_index:]
    crates_in_trasit.reverse()
    stack_assignment[destination_stack].extend(crates_in_trasit)
    for x in range(move_to_do):
        stack_assignment[starting_stack].pop()

    number_of_moves.pop(0)
    origin_stack.pop(0)
    target_stack.pop(0)


# Read the top (last) letter of the 9 crate stacks and print it out

crate_config = []

crate_config.append(stack_1[-1])
crate_config.append(stack_2[-1])
crate_config.append(stack_3[-1])
crate_config.append(stack_4[-1])
crate_config.append(stack_5[-1])
crate_config.append(stack_6[-1])
crate_config.append(stack_7[-1])
crate_config.append(stack_8[-1])
crate_config.append(stack_9[-1])


print(crate_config)