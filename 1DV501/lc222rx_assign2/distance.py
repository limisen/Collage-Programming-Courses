# A program that calculates the distance between two points
from math import sqrt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

distance = sqrt((x1-x2)**2 + (y1-y2)**2)

print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {distance:.3f}")
