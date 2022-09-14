nr = int(input("Please provide an integer: "))

if nr > 0:
    print(str(nr) + " is positive")
elif nr < 0:
    print(str(nr) + " is negative")
else:
    print(str(nr) + " is zero, neither negative or positve")
