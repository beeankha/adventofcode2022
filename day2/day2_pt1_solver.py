# Read input file
f = open("day2_input.txt", "r")
input_list = []
for i in f.read().split("\n"):
    if not i:
        continue
    input_list.append(i)

# variables for choices
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# scores
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

rocktie = 'A X'
papertie = 'B Y'
scissorstie = 'C Z'

rockwin = 'C X'
paperwin = 'A Y'
scissorswin = 'B Z'

rockloss = 'B X'
paperloss = 'C Y'
scissorsloss = 'A Z'

scorelist = []

for combo in input_list:
    if combo == rockloss:
        score = 1
        scorelist.append(score)
    elif combo == paperloss:
        score = 2
        scorelist.append(score)
    elif combo == scissorsloss:
        score = 3
        scorelist.append(score)
    elif combo == rocktie:
        score = 4
        scorelist.append(score)
    elif combo == papertie:
        score = 5
        scorelist.append(score)
    elif combo == scissorstie:
        score = 6
        scorelist.append(score)
    elif combo == rockwin:
        score = 7
        scorelist.append(score)
    elif combo == paperwin:
        score = 8
        scorelist.append(score)
    elif combo == scissorswin:
        score = 9
        scorelist.append(score)
    

grandtotal = sum(scorelist)
print(grandtotal)
