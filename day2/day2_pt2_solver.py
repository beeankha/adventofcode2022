# Read input file
f = open("day2_input.txt", "r")
input_list = []
for i in f.read().split("\n"):
    if not i:
        continue
    input_list.append(i)

# variables for choices
# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

# scores
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

rocktie = 'A Y'
papertie = 'B Y'
scissorstie = 'C Y'

rockwin = 'C Z'
paperwin = 'A Z'
scissorswin = 'B Z'

rockloss = 'B X'
paperloss = 'C X'
scissorsloss = 'A X'

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
