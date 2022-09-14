# To sumerize this program seperates the integer given into 3 seperate numbers,
# hundreds, tens and ones. Ex: 425; hundreds = 4, tens = 2 and ones = 5
# Then sums the numbers up, to continue with the example 4+2+5 = 11
nr = int(input("Provide a three digit number please: "))

# hundreds
hundreds = int(nr % 100)
hundreds = nr - hundreds
hundreds = hundreds // 100
# print("hundreds: ", hundreds)

# tens:
tens = nr - (nr - int(nr % 100))
tens = tens // 10
# print("tens: ", tens)

# ones:
ones = nr - (nr - int(nr % 100))
ones = ones % 10
ones = ones
# print("ones: ", ones)

# Diplays the output
print("The sum of the given numbers: " + str(hundreds + tens + ones))
