# A*x**2 + B*x + C = 0
from math import sqrt


A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

x = ((-1* B) + sqrt(B*2 - 4*A*C )) / (2*A)
z = ((-1 * B) - sqrt(B*2 - 4*A*C)) / (2*A)

#print(x, z, sep=" ")

if A <= 0 or B <= 0 or C <= 0:
    print("There are no solutions")
else:
    print("There are two solutions, namely " + str(x) + " and " + str(z))