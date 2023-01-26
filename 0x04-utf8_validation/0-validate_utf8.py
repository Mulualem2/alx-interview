#!/usr/bin/python3
""" python code that given a data set checks if is a valid UTF-8"""


def validUTF8(data):
    """ determine if a given data set is a valid UTF-8 encoding """
    nbrOfbytes = 0
    for i in data:
        """check how many initial bits are set in data"""
        mask = 1 << 7
        if nbrOfbytes == 0:
            while mask & i:
                nbrOfbytes = nbrOfbytes + 1
                mask = mask >> 1
            if nbrOfbytes == 0:
                continue
            elif nbrOfbytes == 1 or nbrOfbytes > 4:
                return False
        else:
            """Check if the most significant bit is a 1 and
              the second most significant bit is a 0"""
            if not (i & 1 << 7 and not (i & 1 << 6)):
                return False
        nbrOfbytes = nbrOfbytes - 1
    if nbrOfbytes == 0:
        return True
    return False
