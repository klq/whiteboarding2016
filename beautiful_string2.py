import sys
from collections import Counter


with open(sys.argv[1],'r') as f:
    for line in f:
        cnt = Counter()
        s = [char.lower() for char in line if char.isalpha()]

        for c in s:
            cnt[c] += 1

        weight = 26
        score = 0

        for e in cnt.most_common():
            score += weight * e[1]
            weight -=1

        print score





    
