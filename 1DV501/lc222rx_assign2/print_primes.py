# A program that asks for a number of prime numbers to print.
# The program then prints them ten at a line and continues
# on the next line untill the amount equalls the requested amount.

n = int(input("How many primes? "))
amount = 0
z = 0
number = 0

while amount != n:
    number += 1
    if number > 1:
        for div in range(2, number):
            if (number % div) == 0:
                break
        else:
            z += 1
            amount += 1
            if z == 11:
                z = 1
                print("")
            print(number, end=" ")
