# Asks for a number of values to be generated. Then presents said values.
# Before calculating the avrage, minimum and maximum of the generated values.
from random import randrange

n = int(input("Enter number of integers to be generated: "))
print("")

maxi = 0
mini = 101
avg = 0

print("Generated values: ", end="")
for i in range(0, n + 1):
    rng = randrange(1, 100)
    print(rng, end=" ")
    if rng > maxi:
        maxi = rng
    elif rng < mini:
        mini = rng
    avg += rng
avg = avg/n
print("")

print("Average, min, and max are: ", end="")
print("{0:.1f}, {1} and {2}".format(avg, mini, maxi))
