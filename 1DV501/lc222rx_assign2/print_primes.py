# A program that asks for a number of prime numbers to print.
# The program then prints them ten at a line and continues
# on the next line.

n = int(input("How many primes? "))
nr = 0
x = 0
i = 0
con_x = 0

while nr != n:
    i += 1
    con_x = 0
    for div in range(1, i):
        if (i % div) != 0:
            con_x = 1
        else:
            con_x = 0

    if (i % 2) != 0 and i % i == 0 and con_x == 1:
        print(i, end=" ")
        nr += 1
        x += 1
    if x == 10:
        print("")
        x = 0
