# A converted program that uses a for loop instead of a while loop
count = 0
total = 0

# The while loop;
while count < 100:
    total = total + count
    count = count + 1

print("While: " + str(total))
# End of the while loop and it concerning

# The converted (now for) loop;
total = 0
for n in range(100):
    total = total + n
print("For: " + str(total))
