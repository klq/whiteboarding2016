'''
@talky
def square(x):
    return x * x

answer = square(5)

You get the following output:

Oh hi!
The result sure is 25!
'''

def talky(func):
  def func_wrapper(x):
    return "Hi there, the answer sure is: {0}".format(func(x))
  return func_wrapper

def talky_with(name):
  def talky_with_name(func):
    def func_wrapper(x):
      print "Hi there. This is {0} !\nThe answer sure is: {1} ".format(name, func(x))
      return ''
    return func_wrapper
  return talky_with_name


# @talky
@talky_with("Aaron")
def square(x):
  return x * x

print square(5)
