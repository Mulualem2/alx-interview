#!/usr/bin/python3
"""Given consecutive integers starting from 1 up to and including n"""


def isWinner(x, nums):
    """Given consecutive integers starting from 1 up to and including n"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i*i, n + 1, i):
            sieve[j] = False

    sieve[0] = sieve[1] = False
    c = 0
    for i in range(len(sieve)):
        if sieve[i]:
            c += 1
        sieve[i] = c

    winner = ''
    player1 = 0
    for n in nums:
        player1 += sieve[n] % 2 == 1
    if player1 * 2 == len(nums):
        winner = None
    if player1 * 2 > len(nums):
        winner = "Maria"
    else:
        winner = "Ben"
    return winner
