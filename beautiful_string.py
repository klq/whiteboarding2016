#2-1-2016
'''
https://www.codeeval.com/open_challenges/83/
'''

import string
from collections import defaultdict

lines = ['ABbCcc',
'Good luck in the Facebook Hacker Cup this year!',
'Ignore punctuation, please :)',
'Sometimes test cases are hard to make up.',
'So I just go consult Professor Dalves']

for line in lines:
  if line:
    line = line.translate(None,string.punctuation)

    beauty_dict = defaultdict(int)
    for letter in line.replace(' ','').lower():
      beauty_dict[letter] += 1

  beauty = 0
  weight = 26
  for count in sorted(beauty_dict.values(),reverse=True):
    beauty += count * weight
    weight -= 1

  print beauty



