saving = 1000
interest = 1.09
years = 5

newVal = saving * (interest ** years)
newVal = round(newVal)

print("Initial savings: " + str(saving))
print("Interest rate: " + str(interest))
print("Number of years: " + str(years))
print("The value of your savings after " + str(years) + " years is: " + str(newVal))
