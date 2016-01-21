'''
Write a program that reads from standard input and writes each line reversed to standard output. 
For example, if your Python script is called "reverser.py", you could do this at a command line:

echo -e "first line\nsecond line" | python reverser.py

And the output should be:
enil tsrif
enil dnoces
'''

import sys

s = sys.stdin.read()
lines = s.splitlines()
for l in lines:
    print l[::-1]

# for line in sys.stdin.read():
#     print line[::-1].strip('\n')