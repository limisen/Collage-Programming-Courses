#
n = int(input("Enter a positive integer: "))
largest = 0
total = []

if n <= 1:
    n = int(input("Please provide a POSITVE INTEGER: "))

for k in range(0,n, 2):
    total.append(k)
    print(total)
    for i in range(len(total)):
        largest += total[i]
        if largest >= n:
            break
    if largest >= n:
        break
print((str(largest) + " is the largest n such that 0+2+4+6+...+ k < " + str(n)))