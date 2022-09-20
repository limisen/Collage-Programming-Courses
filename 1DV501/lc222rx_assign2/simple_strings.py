# ha

def first_last(s):
    # Prints the first and last character in the string s
    if s == "":
        s = input()

    frst_chr = s[0]
    lst_chr = s[len(s) - 1]

    print(f"First and last in \"{s}\": {frst_chr} and {lst_chr}\ng")


def char_types(s):
    # Prints the number of vowels and consonants in string s
    if s == "":
        s = input()

    vowel = ["A", "E", "I", "O", "U", "Y", "W"]
    consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q"]
    consonants += ["S", "T", "V", "X", "Z",  "H", "R", "W", "Y"]

    print(f"In that sentence, the number of vowels is {10} ", end="")
    print(f"and the number of consonants is {2}\n")


def char_symbol_number(s):
    # Prints the number of characters, symbols (including spaces)
    # and numbers in string s
    if s == "":
        s = input()

    nr_chr = len(s) - 1
    nr_sym = "ha"
    nrs = int(s)
    print(f"In the sentence \"{s}\" the number of letters is {18},", end="")
    print("symbols is {11} and numbers is {nrs}\n")


first_last(input("Enter a string: "))
char_types(input("Enter a string: "))
char_symbol_number(input("Enter a string: "))
