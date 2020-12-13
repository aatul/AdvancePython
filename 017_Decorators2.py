"""
A Python program to demonstrate that a function can be defined inside another function and a function can be passed as parameter.
"""

# Adds a welcome message to the string 
def messageWithWelcome(str): 

	# Nested function 
	def addWelcome(): 
		return "Welcome to "

	# Return concatenation of addWelcome() 
	# and str. 
	return addWelcome() + str

# To get lang name to which welcome is added 
def lang(lang_name): 
	return lang_name 

print (messageWithWelcome(lang("Python 3")))
