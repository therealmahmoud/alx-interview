#!/usr/bin/python3
""" An alx interview preparation question. """


def minOperations(n):
    """ Calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    count = 0
    copy = ""
    char = "H"
    for _ in range(n):
        if len(char) >= n:
            break
        if len(char) + len(copy) == n:
            char + copy
            count += 1
            break
        if len(char) % 2 != 0:
            if len(char) > n:
                break
            count += 2
            copy = char
            char += copy
        if len(char) % 2 == 0:
            if len(char) > n:
                break
            char += copy
            count += 1
    return count
