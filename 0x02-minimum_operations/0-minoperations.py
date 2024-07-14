#!/usr/bin/python3
""" An alx interview preparation question. """


def minOperations(n: int) -> int:
    """ Calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    count: int = 0
    copy: int = 0
    char: int = 1
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
