# ha

import re


def first_last(s):
    # Prints the first and last character in the string s
    if s == "":
        s = input("Please enter a string: ")

    frst_chr = s[0]
    lst_chr = s[len(s) - 1]

    print(f"First and last in \"{s}\": {frst_chr} and {lst_chr}\n")


def char_types(s):
    # Prints the number of vowels and consonants in string s
    if s == "":
        s = input("Please enter a string: ")

    vowel = ["A", "E", "I", "O", "U", "Y", "W", 'a', 'e', 'i' 'o', 'u', 'y']
    v = 0
    consonants = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q"]
    consonants += ["S", "T", "V", "X", "Z",  "H", "R", "W", "Y"]
    consonants += ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm']
    consonants += ['n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    c = 0

    for i in range(0, len(s)):
        for n in range(0, len(vowel)):
            if s[i] == vowel[n]:
                v += 1
    for i in range(0, len(s)):
        for n in range(0, len(consonants)):
            if s[i] == consonants[n]:
                c += 1

    print(f"In that sentence, the number of vowels is {v} ", end="")
    print(f"and the number of consonants is {c}\n")


def char_symbol_number(s):
    # Prints the number of characters, symbols (including spaces)
    # and numbers in string s
    if s == "":
        s = input("Please enter a string: ")

    nr_chr = len(s)
    nr_sym = []

    for i in range(0, len(s)):
        if not (s[i].isalpha()):
            nr_sym = nr_sym.append(s[i])

    nrs = re.findall('[0-9]+', s)
    print(f"In the sentence \"{s}\" the number of letters is {18},", end="")
    print(f" symbols is {11} and numbers is {len(nrs)}\n")


#first_last(input("Enter a string (F,L): "))
#char_types(input("Enter a string (Types): "))
char_symbol_number(input("Enter a string (sym): "))
