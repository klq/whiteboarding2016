# 1-24-2016
# balanced-parentheses
# A version of this problem was faced at a whiteboard by a Metis student in an interview for a data scientist position on April 16, 2015.

'''
In programming languages, and especially in Lisps, there can be a lot of parentheses. 
The parentheses have to be "balanced" to be valid. For example, ()(()) is balanced, but ()()) is not balanced. Also, )((()) is not balanced.

Write a function that takes a string and returns True if the string's parentheses are balanced, False if they are not.

Test cases:

(()()()()) should return True
(((()))) should return True
(()((())())) should return True
((((((()) should return False
())) should return False
(()()))(() should return False
'''

def balanced_parenthesis(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            try:
                stack.pop()
            except IndexError:
                return 'False'
    return (not stack)  # if stack is [ ], return True


print balanced_parenthesis('(()()()())')
print balanced_parenthesis('(((())))')
print balanced_parenthesis('(()((())()))')
print balanced_parenthesis('((((((())')
print balanced_parenthesis('()))')
print balanced_parenthesis('(()()))(()')


def balanced_parenthesis2(s):
    while "()" in s:
       s = s.replace("()", "")
       
    return (not s)

print balanced_parenthesis2('(()()()())')
print balanced_parenthesis2('(((())))')
print balanced_parenthesis2('(()((())()))')
print balanced_parenthesis2('((((((())')
print balanced_parenthesis2('()))')
print balanced_parenthesis2('(()()))(()')

