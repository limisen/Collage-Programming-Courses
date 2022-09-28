# Eight math functions that do as follows

def inc(n):
    """Increases n with one, n + 1"""
    n += 1
    return(n)


def inc_with(n, t):
    """Increases n with the value of t, n + t"""
    n += t
    return(n)


def dec(n):
    """Decreases n with one, n - 1"""
    n -= 1
    return(n)


def dec_with(n, t):
    "Decreases n with the value of t, n - t"""
    n -= t
    return(n)


def greatest(n1, n2):
    """Returns the largest of the values n1 and n2"""
    if n1 > n2:
        return(n1)
    elif n2 > n1:
        return(n2)


def is_even(n):
    """Returns True if n is even, otherwise False"""
    if (n % 2) == 0:
        return(True)
    else:
        return(False)


def power(x, n):
    """Returns x to the power of n, x**n"""
    return(x**n)


def factorial(n):
    """Returns the factorial of n,\n
    n = 5 \n
    n = 5*4*3*2*1
    """

    x = 1
    for i in range(n, 1, -1):
        x = x * i
    return(x)


print(inc(41))

print(inc_with(30, 12))

print(dec(43))

print(dec_with(52, 10))

print(greatest(24, 42))

print(is_even(42))

print(power(2, 16))

print(factorial(5))
