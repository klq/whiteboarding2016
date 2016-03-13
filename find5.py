'''
If you have a sorted list of numbers, how can you find the number that is
closest to 5 without checking every number? Write pseudo-code for an algorithm.
'''


def find5(l, start, end):

  while start + 1 >= end:
    diff1 = abs(l[start] - 5)
    diff2 = abs(l[end] - 5)
    if diff1 <= diff2:
      print "No 5 found closest numbers is {0}".format(l[start])
      return
    else:
      print "No 5 found closest numbers is {0}".format(l[end])
      return

  mid = ( start + end ) / 2 # rounding down
  print start, end, mid

  if l[mid] == 5:
    return "Found 5 at index {0}!".format(str(mid))

  if l[mid] > 5:
    end = mid

  if l[mid] < 5:
    start = mid

  return find5(l, start, end)


a = [1,1,2,4,4,8,9,10]
print find5(a, 0 , len(a)-1)
