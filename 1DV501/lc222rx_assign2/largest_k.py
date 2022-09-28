# A program (largest_k.py) which for any given positive integer n,
# (read from the keyboard) computes the largest integer k
# such that 0 + 2 + 4 + 6 + 8 + ... + k < n.

n = int(input("Enter a positive integer: "))
largest = 0
total = []

if n <= 1:
    n = int(input("Please provide a POSITVE INTEGER!!!!: "))

for k in range(0,  n, 2):
    total.append(k)
    # print(total)
    largest = 0
    for i in range(len(total)):
        largest += total[i]
        if largest >= n:
            total.pop()
            # print(total)
            break
    if largest >= n:
        break
print(str(total[len(total) - 1]) + " ", end=" ")
print("is the largest n such that 0+2+4+6+...+ k < " + str(n))
