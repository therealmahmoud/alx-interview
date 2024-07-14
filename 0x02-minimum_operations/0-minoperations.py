#!/usr/bin/python3
""" An alx interview preparation question. """


def minOperations(n: int) -> int:
    """ Calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    count: int = 0
    copy: str = ""
    char: str = "H"
    while len(char) < n:
        if len(copy) == 0:
            copy = char
            char += copy
            count += 2
        elif len(char) + len(copy) == n:
            char + copy
            count += 1
            break
        elif len(char) % 2 != 0: # for Odds
            count += 2
            copy = char
            char += copy
        elif len(char) % 2 == 0: # for Even
            char += copy
            count += 1
    return count
