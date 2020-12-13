"""
Decorators in Python

Useful points to understand decorator functions in Python:
1. In Python, we can define a function inside another function.
2. In Python, a function can be passed as parameter to another function (a function can also return another function).
"""

# defining a decorator 
def hello_decorator(func): 

	# inner_function is a Wrapper function in which the argument is called 
	
	# inner function can access the outer local functions like in this case "func" 
	def inner_function(): 
		print("Hello, this is before function execution") 

		# calling the actual function now inside the wrapper function. 
		func() 

		print("This is after function execution") 
		
	return inner_function 


# defining a function, to be called inside wrapper 
def function_to_be_used(): 
	print("This is inside the function !!") 


# passing 'function_to_be_used' inside the decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 


# Driver Code: calling the function 
function_to_be_used() 
