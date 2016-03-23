'''
Write a function that checks if a given sentence is a palindrome. A palindrome is a word, phrase, verse, or sentence that reads the same backward or forward. Only the order of English alphabet letters (A-Z and a-z) should be considered, other characters should be ignored.

For example, is_palindrome('Noel sees Leon.') should return true as spaces, period, and case should be ignored resulting with "noelseesleon" which is a palindrome since it reads same backward and forward.

'''

class Palindrome:

    @staticmethod
    def is_palindrome(text):
        text = ''.join([c for c in text.lower() if c.isalpha()])
        return text == text[::-1]

#To see the output, uncomment the line belows:
print(Palindrome.is_palindrome('Noel sees Leon.'))
