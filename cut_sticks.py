'''
Cut the sticks problem on HackerRank
https://www.hackerrank.com/challenges/cut-the-sticks
'''

n = int(raw_input().strip())
sticks = map(int,raw_input.strip().split(' '))


while len(sticks) > 0:
    print len(sticks)
    sticks = [s - min(sticks) for s in sticks]
    sticks = [s for s in sticks if s > 0]
