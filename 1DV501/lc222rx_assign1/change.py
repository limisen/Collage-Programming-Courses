price = float(input("How much does it cost?: "))
#price = 600

payment_amt = float(input("How much will u pay?: "))
#payment_amt = 1000

if price > payment_amt:
    payment_amt = int(input("Please provide more than the given price: "))

change = payment_amt - round(price) 
print("Change: " + str(int(change)) + "kr")

#Here and below needs work!
x = [1000, 500, 200, 100, 50, 20 , 10, 5, 1]
n = 0
billsum = 0

while n != len(x):
    while billsum != change or n != len(x):
        print(billsum)
        nr = int(change / x[n])
        if nr >= 1 :
            if billsum >= change:
                print("{:=4d}kr bills: {}".format(x[n], 0))
            if billsum + x[n] > change:
                print("{:=4d}kr bills: {}".format(x[n], 0))
            else:
                billsum = billsum + (x[n] * nr)
                print("{:=4d}kr bills: {}       dog".format(x[n], nr))
        else:
            print("{:=4d}kr bills: {}       cat".format(x[n], 0))
        n = n+1
