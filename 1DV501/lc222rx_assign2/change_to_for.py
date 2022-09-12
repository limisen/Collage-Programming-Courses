#A converted program that uses a for loop instead of a while loop
count = 0
total = 0

while count < 100:
    total = total + count
    count = count + 1

print(count)

for n in range(100):
    n += 1
print(n)