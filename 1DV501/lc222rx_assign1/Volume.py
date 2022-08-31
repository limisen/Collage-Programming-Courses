#Importing math since i require the value of pi in order to do a operation further down regarding the spheres volume.
import math

#Aquireing a value for the spheres radius form the user.
r = float(input("Please provide a radius of some sphere: "))

#setting the value to 6 for debug purposes
#r = 6

#formula for the spheres volume
v = V=(4/3) * (math.pi) * (r**3)

#rounding off to a maximum of a single decimal
v = round(v , 1)

print("The volume is " + str(v))