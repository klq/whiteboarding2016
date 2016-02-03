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
email_regex = '[a-zA-Z0-9_]+@[a-zA-Z0-9_].[a-zA-Z]'
with sys.argv[1] open as f:
    for line in f:
        if line:
            re.compile()

