# decorator function to capitalize names

import cProfile
import pstats

def names_decorator(function):
   def wrapper(arg1, arg2, arg3):
       arg1 = arg1.upper()
       arg2 = arg2.capitalize()
       arg3 = arg3.lower()
       string_hello = function(arg1, arg2, arg3)
       return string_hello
   return wrapper
@names_decorator
def say_hello(name1, name2, message):
   return 'Hello ' + name1 + '! Hello ' + name2 + '!' + message
say_hello('sara', 'ansh', "welcome")   # output => 'Hello Sara! Hello Ansh!'
print(say_hello('sara', 'ansh', "welcome") )


# decorator function to convert to lowercase
def lowercase_decorator(function):
   def wrapper():
       func = function()
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper


# decorator function to split words
def splitter_decorator(function):
   def wrapper():
       func = function()
       string_split = func.split()
       return string_split
   return wrapper



@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
   return 'Hello World'
hello()   # output => [ 'hello' , 'world' ]
print(hello())


## generate fibonacci numbers upto n
def fib(n):
    """What are generators in Python?
    Generators are functions that return an iterable collection of items, one at a time, in a set manner."""
    p, q = 0, 1
    while(p < n):
        yield p
        p, q = q, p + q
x = fib(10)    # create generator object 
 
## iterating using __next__(), for Python2, use next()
x.__next__()    # output => 0
x.__next__()    # output => 1
x.__next__()    # output => 1
x.__next__()    # output => 2
x.__next__()    # output => 3
x.__next__()    # output => 5
x.__next__()    # output => 8
#x.__next__()    # error
 
## iterating using loop
for i in fib(10):
   print(i)    # output => 0 1 1 2 3 5 8


cProfile.run('fib(2000)', 'my_profile.prof')

with open('stats.txt', 'w') as f:
    stats = pstats.Stats('my_profile.prof', stream=f)
    stats.sort_stats('cumulative')
    stats.print_stats()