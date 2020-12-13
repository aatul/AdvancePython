"""
Decorators with parameters in Python

Python functions are First Class citizens which means that functions can be treated similar to objects.

1. Function can be assigned to a variable i.e they can be referenced.
2. Function can be passed as an argument to another function.
3. Function can be returned from a function.

"""

def decorator(*args, **kwargs): 
	print("Inside decorator") 
	def inner(func): 
		print("Inside inner function") 
		print("I like", kwargs['like']) 
		return func 
	return inner 

@decorator(like = "Python") 
def func(): 
	print("Inside actual function") 

func() 
