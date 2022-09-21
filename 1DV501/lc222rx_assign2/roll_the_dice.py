# A program that throws a dice a number of times.
# Then calculates the difference of the most and lest common die face.
# Then calculates a sort of ratio said differnce
from random import randrange

head_of_dice = [0, 0, 0, 0, 0, 0]

print("start: ")


def roll_x_times(x):
    for i in range(0, x):
        roll = randrange(1, 7)
        if roll == 1:
            times = head_of_dice[0] + 1
            head_of_dice[0] = times
        elif roll == 2:
            times = head_of_dice[1] + 1
            head_of_dice[1] = times
        elif roll == 3:
            times = head_of_dice[2] + 1
            head_of_dice[2] = times
        elif roll == 4:
            times = head_of_dice[3] + 1
            head_of_dice[3] = times
        elif roll == 5:
            times = head_of_dice[4] + 1
            head_of_dice[4] = times
        elif roll == 6:
            times = head_of_dice[5] + 1
            head_of_dice[5] = times


i = 10
for n in range(20):
    roll_x_times(i)
#      print(f"result: {head_of_dice}")
    mini = min(head_of_dice)
    maxi = max(head_of_dice)
    if mini == 0 or maxi == 0:
        procent = 100
    elif mini == maxi:
        procent = 100
    else:
        diff = maxi - mini
        procent = diff/maxi * 100
#      print(f"Procent: {procent}")
    print("for {:7} rolls, the difference is {:.1f}%".format(i, procent))
    i *= 2
