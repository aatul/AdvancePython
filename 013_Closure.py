"""
CLOSURE

A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Let us get to it step by step

Firstly, a Nested Function is a function defined inside another function. It's very important to note that the nested functions can access the variables of the enclosing scope. However, at least in python, they are only readonly. However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.


"""

def outer_function(message):
  "This is the enclosing/outer function"
  def inner_function():
      "The nested/inner function"
      print(message)
  return inner_function

test = outer_function("Hello Python!")
test()

"""
Even though the execution of the "outer_function()" was completed, the message was rather preserved. This technique by which the data is attached to some code even after end of those other original functions is called as closures in python

ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.(Eg. When there are few methods in a class, use closures instead).

Also, Decorators in Python make extensive use of closures.
"""