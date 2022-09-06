x = int(input("Please provide your monthly income: "))

if x <= 38000:
    tax = x * 0.3
elif x >= 38000 and x <= 50000:
    tax = x * 0.3
    tax = tax + ((x - 38000) * 0.05)
else:
    tax = x * 0.3
    tax = tax + ((x - 38000) * 0.05) + ((x - 50000) * 0.05)

print("Corresponding income tax: " + str(int(tax)))