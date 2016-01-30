# 1-24-2016
# Euler #3 https://projecteuler.net/problem=3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
See if you can optimize your solution. What is the complexity of your program?
'''

import time
import math

def euler3():
    n = 600851475143
    i = 2
    while i*i < n:
        while n % i == 0:
            print str(i) + " is a factor"
            n = n/i
        i += 1
            
    print str(n) + " is a factor"
    return  n 

start_time = time.time()
euler3()
time_elapsed = time.time() - start_time

print time_elapsed
