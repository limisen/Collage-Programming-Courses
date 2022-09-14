fname = input("First name: ")
Mname = input("Middle name: ")
Lname = input("Last name: ")

if Mname == (""):
    print("Short name: " + str(fname[0]) + ". " + Lname)
else:
    print("Short name: " + str(fname[0]) + ". " + str(Mname[0]) + ". " + Lname)
