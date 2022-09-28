# A random number is generated then added to a list. Then it calculates the
# avrage by first adding each nr as it gets generated to the "nrs"-list,
# then devides it by how ever many nrs the list contains
# minimum and maximum and secound maximun of the generated value.
from random import randrange

nrs = []
avg = 0

for i in range(0, 10):
    rng = randrange(1, 10000)
    nrs.append(rng)
    avg += rng
    print(nrs)
avg = avg/len(nrs)

nrs.sort(reverse=True)

print("Largest value in list: {0}".format(nrs[0]))
print("Smallest value in list: {0}".format(nrs[len(nrs) - 1]))
print("Average value in list: {0:.1f}".format(avg))
print("Second largest value in list: {0}".format(nrs[1]))
