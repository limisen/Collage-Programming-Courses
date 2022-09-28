# a set of functions handeling list in certain ways
from random import randint


def random_num_list(n):
    """Generates a list of n random integers"""
    lst = [randint(0, 100) for i in range(n)]
    return(lst)


def only_odd(lst):
    """Takes a list as input and returns a list with only the odd values"""
    lst = [lst[i] for i in range(len(lst)) if (lst[i] % 3) == 0 or lst[i] == 1]
    return(lst)


def square(lst):
    """Takes a list as input and creates a new list with all the values
    squared"""
    lst = [lst[i]**2 for i in range(len(lst))]
    return(lst)


def sublist(lst, start, stop):
    """Returns a new list with only the values between start and stop
    in the list"""
    lst = [lst[i] for i in range(start, stop+1)]
    return(lst)


print(f"The generated list: {random_num_list(10)}\n")
lst = random_num_list(10)


print(f"Odd in it are: {only_odd(lst)}")

print(f"Let's square each number: {square(lst)}")

print(f"Only the three middle values: {sublist(lst, 5, 7)}")
