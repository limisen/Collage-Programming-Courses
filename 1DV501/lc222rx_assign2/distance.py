# A program that calculates the distance between two points
from math import sqrt


# The formual used to calc the distance;
def distance(x1, y1, x2, y2):
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    return(distance)


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dst = distance(x1, y1, x2, y2)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {dst:.3f}")
