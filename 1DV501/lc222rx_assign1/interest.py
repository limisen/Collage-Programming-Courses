#This program calculates the value of inital savings given certain interest percentages
saving = int(input("Start value of savings: "))
interest = int(input("Please provide the interest rate (in percentages): "))
interest = (interest/100) + 1
years = 5

newVal = saving * (interest ** years)
newVal = round(newVal)

print("Initial savings: " + str(saving))
print("Interest rate: " + str(interest))
print("Number of years: " + str(years))
print("The value of your savings after " + str(years) + " years is: " + str(newVal))
