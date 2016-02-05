# 2-2-2016
'''
You are given several strings that may/may not be valid emails.
You should write a regular expression that determines if the email id is a valid email id or not.
You may assume all characters are from the english language.

Print out 'true' (all lowercase) if the string is a valid email. Else print out 'false' (all lowercase). E.g.

https://www.codeeval.com/open_challenges/35/

foo@bar.com
this is not an email id
admin#codeeval.com
good123@bad.com

true
false
false
true
'''

# at least one @
# some characters before @
# some characters after @ followed by a .
# some characters after the .

import sys
import re


# building a regular expression
email_regex = re.compile(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+.[a-zA-Z]+(.[a-zA-Z]+)*$')

with open(sys.argv[1],'r') as f:
    for line in f:
      line = line.rstrip()
      if line:
        if email_regex.match(line):
          print 'true'
        else:
          print 'false'


#Code eval test cases:
'''
Abc.example.com
hfij#kjdfvkl
very.common@example.com
A@b@c@example.com
niceandsimple@example.com
this is not true
b@domain.net
disposable.style.email.with+156@example.com
just"not"right@example.com
<invalid>@foo.com
a"b(c)d,e:f;g<h>i[j\k]l@example.com
"very.unusual.@.unusual.com"@example.com
a.little.lengthy.but.fine@dept.example.com
this is"not\allowed@example.com
b@d.net
asterisk_domain@foo.*
1@d.net
bob123@alice123.com
this\ still\"not\\allowed@example.com
disposable.style.email.with+symbol@example.com
'''

