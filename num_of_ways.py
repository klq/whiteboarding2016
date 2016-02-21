'''
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent)
write code to calculate the number of ways of representing n cents.

'''

def ways(cents, coins=[25, 10, 5, 1]):
    """Return the number of ways to make change.

    >>> ways(100)
    242
    """
    if cents < 0:
        return 0

    if cents == 0 or cents == 1:
        return 1

    return ways(cents-25) + ways(cents-10) + ways(cents-5) + ways(cents-1)

print ways(10)

