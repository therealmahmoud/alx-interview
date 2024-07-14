#!/usr/bin/python3
""" An alx interview preparation question. """


def minOperations(n: int) -> int:
    """ Calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    count: int = 0
    copy: str = ""
    char: str = "H"
    for _ in range(n):
        if len(char) >= n:
            return 0
        if len(char) + len(copy) == n:
            char + copy
            count += 1
            break
        if len(char) % 2 != 0:
            if len(char) > n:
                return 0
            count += 2
            copy = char
            char += copy
        if len(char) % 2 == 0:
            if len(char) > n:
                return 0
            char += copy
            count += 1
    return count
