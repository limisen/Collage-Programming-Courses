#
n = int(input("How many primes? "))

if n < 2:
    print("Please provide a PRIME integer! ")
else:
    prime = True

    for i in range(2, n):
        if n%i == 0:
            prime = False
            break
        if prime:
            print(n, "is a prime number")
        else:
            print(n, "is not a prime number. it is divisable by ", i)