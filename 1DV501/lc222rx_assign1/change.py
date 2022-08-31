price = float(input("How much does it cost?: "))
#price = 600

payment_amt = float(input("How much will u pay?: "))
#payment_amt = 1000

if price > payment_amt:
    payment_amt = int(input("Please provide more than the given price: "))

change = payment_amt - round(price) 
print("Change: " + str(int(change)) + "kr")

x = [2, 2, 2.5, 2, 2, 2.5, 2 ,2 , 2.5, 2]
y = 0
z = 2000
n = 0


for n in range(0,10):
    a = 0
    while a != change:
        z = z / x[n] 
        nr = int(z // z)
        print(str(z) + "kr bills: " + str(nr))
        n = (n+1)
        a = z + z
