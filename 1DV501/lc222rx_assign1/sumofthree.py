#Note: you may not convert the input from an integer to a string or a list, or anything else, you need to calculate the answer!

from decimal import ROUND_DOWN


nr = int(input("Provide a three digit number please: "))

hundreds = nr / 100
print(hundreds)
tens = nr / 10
print(tens)
tens = nr / 100
print(tens)
tens = ROUND_DOWN(tens)
print(tens)
