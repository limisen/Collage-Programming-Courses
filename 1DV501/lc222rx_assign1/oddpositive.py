from random import randint  

rng = randint(-10, 10)

if (rng%2) ==  1 and rng > 0:
    print(str(rng) + " is odd and positive")
elif (rng%2) ==  0 and rng > 0:
    print(str(rng) + " is even and positive")
elif (rng%2) ==  1 and rng < 0:
    print(str(rng) + " is odd and negative")
elif (rng%2) ==  0 and rng < 0:
    print(str(rng) + " is even and negative")