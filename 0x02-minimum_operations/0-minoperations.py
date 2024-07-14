#!/usr/bin/python3
""" An alx interview preparation question. """


def minOperations(n):
    """ Calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    if not isinstance(n, int):
        return 0
    count = 0
    copy = 0
    char = 1
    while char < n:
        if copy == 0:
            copy = char
            char += copy
            count += 2
        elif n - char > 0 and (n - char) % char == 0:
            copy = char
            char += copy
            count += 2
        elif copy > 0:
            char += copy
            count += 1
    return count
