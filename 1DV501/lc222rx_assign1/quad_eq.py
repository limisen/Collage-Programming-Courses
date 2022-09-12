# A*x**2 + B*x + C = 0
from math import sqrt


A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

sol_1 = ((-1* B) + sqrt(B*2 - 4*A*C )) / (2*A)      #Solution 1
sol_2 = ((-1 * B) - sqrt(B*2 - 4*A*C)) / (2*A)      #Solution 2
formula = ((A*x)**2 + (B*x) + C)                      #Formula

#print(x, z, sep=" ")

if A < 0 or B < 0 or C < 0:
    print("There are no solutions")
if A == 0 or B == 0 or C == 0:
    print("There is one solutions " + "(value)")
else:
    print("There are two solutions, namely " + str(sol_1) + " and " + str(sol_2))