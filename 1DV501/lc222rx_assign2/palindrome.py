# is_palindrome takes in a string as its "s" variable and then makes it into
# two strings in, one starting with the first chr in the string and the other
# with the last. Then compares them to see if they are equivilant, if so
# it returns true otherwise false.

def is_palindrome(s):
    s = s.lower()
    s = s.strip()
    l1 = []
    l2 = []

    for i in range(0, len(s)):
        if (s[i].isalpha()):
            l1.append(s[i])
    for i in range(len(s) - 1, -1, -1):
        if (s[i].isalpha()):
            l2.append(s[i])

    if l1 == l2:
        return(True)
    else:
        return(False)


print(is_palindrome(input("Please provide a palindrome (or not): ")))
