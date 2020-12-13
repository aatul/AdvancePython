"""
Function Decorator

A decorator is a function that takes a function as its only parameter and returns a function. This is helpful to “wrap” functionality with the same code over and over again. For example, above code can be re-written as following.
"""

# Adds a welcome message to the string returned by fun(). Takes fun() as parameter and returns welcome(). 
def decorate_message(fun): 

	# Nested function 
	def addWelcome(lang_name): 
		return "Welcome to " + fun(lang_name) 

	# Decorator returns a function 
	return addWelcome 

@decorate_message
def lang(lang_name): 
	return lang_name 

# Driver code 

# This call is equivalent to call to decorate_message() with function lang("Python 3") as parameter 
print (lang("Python 3"))
