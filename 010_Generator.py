"""
Generator in Python

A generator in Python is a function with unique abilities. We can either suspend or resume it at run-time. It returns an iterator object which we can step through and access a single value in each iteration.

Basically the generator provides a way of creating iterators. It solves the following common problem:

    1. In Python, it is cumbersome to build an iterator. First, we require to write a class and implement the __iter__() and __next__() methods.
    
    2. We need to manage the internal states and throw StopIteration exception when there is no element to return.

* How To Create A Generator In Python?
Python generator gives an alternative and simple approach to return iterators. The procedure to create the generator is as simple as writing a regular function.

There are two ways to create generators in Python.

1. Generator Function
    We write a generator in the same style as we write a user-defined function.

    The difference is that we use the yield statement instead of the return. It notifies Python interpreter that the function is a generator and returns an iterator.

2. Generator Expression
    Python allows writing generator expressions to create anonymous generator functions.

    This procedure is similar to a lambda function creating an anonymous function.

    The syntax of a generator expression is the same as of list comprehension in Python. However, the former uses the round parentheses instead of square brackets.
"""

# Example for Generator Function
def fibonacci(num):
    # first two numbers
    x1 = 0
    x2 = 1
    count = 0

    if num <= 0:
       print("Please provide a positive integer")
    elif num == 1:
       print("Fibonacci sequence upto",num,":")
       print(x1)
    else:
       while count < num:
           xth = x1 + x2
           x1 = x2
           x2 = xth
           count += 1
           yield xth

f = fibonacci(5)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

# Use generator expression 
gen_exp = (x for x in range(10))
for x in gen_exp:
    print(x,end=' ')