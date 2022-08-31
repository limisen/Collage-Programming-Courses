#Note: you may not convert the input from an integer to a string or a list, or anything else, you need to calculate the answer!

#Note: This is a VG task, it may be skipped if so desired 

nr = int(input("Provide a three digit number please: "))

#hundreds
hundreds = int(nr % 100)
hundreds = nr - hundreds
hundreds = hundreds // 100
print("hundreds: ", hundreds)

#tens:
tens =  nr - (nr - int(nr % 100))
tens = tens // 10 
print("tens: ", tens)

#ones:
ones = nr - (nr - int(nr % 100))
ones = ones % 10
ones = ones
print("ones: ", ones)

#Desierd output
print("The sum of the given numbers: " + str(hundreds + tens + ones))