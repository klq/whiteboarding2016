#1-22-2016
'''
The data for this problem are the numbers 2, 7, 1, 5, and 10.
We want to know which of the numbers from 0 to 10 (by tenths) gives the smallest result when we do the following:

For each of the numbers in the data, subtract the candidate number and then square the result, then add up these numbers.

For example, to test the candidate number 8.2, we do the following:

2 - 8.2 = -6.2
         (-6.2)**2 = 38.44
7 - 8.2 = -1.2
         (-1.2)**2 = 1.44
1 - 8.2 = -7.2
         (-7.2)**2 = 51.84
5 - 8.2 = -3.2
         (-3.2)**2 = 10.24
10 - 8.2 = 1.8
           1.8**2  = 3.24

38.44 + 1.44 + 51.84 + 10.24 + 3.24 = 105.2
For candidate number 8.2, the result is 105.2. Can we get a smaller result for any of the other candidate numbers? 
Try them all and find the candidate number that gives the smallest result.

You might identify a shortcut to solving this problem. Write the code to try all the candidate numbers anyway.
Once you have an answer, also make a plot to show the results for all the candidate numbers.
As an extension, consider what class of problem this exercise represents. 
Can you write a general solution? Can you write a faster general solution?
'''

import numpy
# result = 5 x^2 - 50 x + 179
def function_result(candidate_number):
    data_numbers = [2, 7, 1, 5, 10]
    return sum([ (candidate_number-x)**2 for x in data_numbers])

result_list = []
for candidate_number in numpy.arange(0,10.1,0.1):
    result_list.append(function_result(candidate_number))
print min(result_list)


