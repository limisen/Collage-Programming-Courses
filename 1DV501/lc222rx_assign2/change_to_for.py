# A converted program that uses a for loop instead of a while loop
count = 0
total = 0

# The while loop;
while count < 100:
    total = total + count
    count = count + 1

print("While: " + str(count))
# End of the while loop and it concerning

# The converted (now for) loop;
for n in range(100):
    n += 1
print("For: " + str(n))
