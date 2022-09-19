# To sumerize this program checks each number in the given integer.
# odds, evens and zeros. Ex: 603425; odds = 2, evens = 3 and zeros = 1
# It goes through and checks if the nr is a zero
# then if its even and if not makes sure its odd
# after that it adds to the correct catergory the nr falls into.
nr = input("Provide a LARGE digit number please: ")

list(nr.strip(" "))

even = 0
odd = 0
zero = 0

for i in range(len(nr)):
    x = int(nr[i])
    if x == 0:
        zero += 1
    elif (x % 2) == 0:
        even += 1
    elif (x % x) == 0:
        odd += 1

# Diplays the output
print(f"\nZeros: {zero}")
print(f"odd: {odd}")
print(f"even: {even}")
