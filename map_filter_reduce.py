x = range(100)

y = reduce(lambda x,y:x+y, filter(lambda x:x%2==0, map(lambda x:x**2, x)))

print y

