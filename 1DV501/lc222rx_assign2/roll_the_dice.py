# haha
from random import randrange

head_of_dice = [0, 0, 0, 0, 0, 0]
print(head_of_dice)

for i in range(0, 10):
    roll = randrange(1, 6)
    print(roll)
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
print(head_of_dice)
