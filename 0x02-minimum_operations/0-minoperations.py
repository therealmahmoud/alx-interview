#!/usr/bin/python3
""" An alx interview preparation question. """


def minOperations(n) -> int:
    """ Calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    if not isinstance(n, int):
        return 0
    count: int = 0
    copy: str = ""
    char: str = "H"
    while len(char) < n:
        if len(char) + len(copy) == n:
            char + copy
            count += 1
            break
        elif len(char) % 2 != 0:
            count += 2
            copy = char
            char += copy
        elif len(char) % 2 == 0:
            char += copy
            count += 1
    return count
