#1-31-2016

'''
In this challenge you need to find the longest word in a sentence. 
If the sentence has more than one word of the same length you should pick the first one.
https://www.codeeval.com/open_challenges/111/

Inputs:
some line with text
another line

Outputs:
some
another
'''

import sys

with open(sys.argv[1],'rb') as f:
    for line in f:
        if line:
            words = line.split()
            lengths = map(len, words)
            max_length = max(lengths)
            max_index = lengths.index(max_length)

            print  words[max_index]
