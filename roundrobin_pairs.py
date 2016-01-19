# Round-robin Problem
# 2016-1-19
'''
Create non-repeating groups of 2 for pair-programming schedules
Using the round-robin implementation found here: 
http://stackoverflow.com/questions/14169122/generating-all-unique-pair-permutations
'''

from collections import deque
import pprint

names = ['Jeffrey','Ben','David','Andres','Shivani','Matteo','Mark','Rui','Ryan','Chris','Do','Matt','George','Ted','Nathan','Nick']

def round_robin_even(d, n):
    for i in range(n - 1):
        yield [[d[j], d[-j-1]] for j in range(n/2)]
        d[0], d[-1] = d[-1], d[0]
        d.rotate()

def round_robin_odd(d, n):
    for i in range(n):
        yield [[d[j], d[-j-1]] for j in range(n/2)]
        d.rotate()

def round_robin(names):
    d = deque(names)
    n = len(names)
    if n % 2 == 0:
        return list(round_robin_even(d, n))
    else:
        return list(round_robin_odd(d, n))

pprint.pprint round_robin(names)
