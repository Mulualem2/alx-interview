#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """draws a pascal triangle 
       and returns it as a list"""
    plist = []

    if n <= 0:
        return plist

    for i in range(n):
        temp = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                temp.append(1)
            else:
                temp.append(plist[i-1][j-1] + plist[i-1][j])
        plist.append(temp)
    return plist
