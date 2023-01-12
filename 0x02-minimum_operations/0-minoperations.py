#!/usr/bin/python3
"""File that uses the min of operations"""


def minOperations(n):
    """
    given a number n, this method calculates the fewest name of operations
    """
    copyPaste = 2
    Paste = 1
    numofops = 0
    totalH = 1
    hPrev = 1

    if n <= 1:
            return 0

    while totalH < n:
            if totalH == 1:
                numofops += copyPaste
                totalH = totalH + totalH
            elif n % totalH == 0 and totalH * 2 <= n:
                numofops += copyPaste
                hPrev = totalH
                totalH = totalH + totalH
            else:
                totalH += hPrev
                numofops += Paste
    return numofops
