#2-1-2016
'''
https://www.codeeval.com/open_challenges/83/
'''

from collections import defaultdict

lines = ['ABbCcc',
'Good luck in the Facebook Hacker Cup this year!',
'Ignore punctuation, please :)',
'Sometimes test cases are hard to make up.',
'So I just go consult Professor Dalves',
"""+_W|F!WwA+n3i|~jV?2%|<YhBxg$5?OLtOCeqfEW9!ICcD,a;bU/69T9V:-5l`\EU$;@]]>xQE\i>S1ehq@btF`I0v@,;5p6WB`3$;pNG!=D#+)eKPr\['UVs,+mHb:7}UOnL'(;`,'f(_[ZIh_Jh|"A8[XB;U]yyv4"Cwhc[zSV0!JVXOEYShNlSt/8Y|Q1i)G~m.izy>3~['yX7yliWx1%rAJ;`Oc33oC?@B)lL95&"""]

for line in lines:
  if line:
    # leave only the alpha characters (no numerals)
    line = ''.join([c for c in line if c.isalpha()])

    beauty_dict = defaultdict(int)
    for letter in line.lower():
      beauty_dict[letter] += 1

  beauty = 0
  weight = 26
  for count in sorted(beauty_dict.values(),reverse=True):
    beauty += count * weight
    weight -= 1

  print beauty



