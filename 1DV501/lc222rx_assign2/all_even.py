#Sums all even numbers up to 100
total = 0
for n in range(0,102, 2):
    total += n
print(("Sum of the 100 first numbers is: " + str(total)))