"""
Two iterators for a single looping construct: In this case, a list and dictionary are to be used for each iteration in a single looping block using enumerate function. Let us see example.
"""

# Define Two separate lists 
lang = ["English", "Hindi", "Marathi", "Arabic"] 
langtype = ["Business Language", "Native Language"] 

# Single dictionary holds characters of lang and its langtype. 
# First three items store characters of lang and next two items store characters of langtype. 
characters = {1:"26", 2:"44", 3:"53", 4:"28", 5:"26", 6:"44"} 

# Printing characters of lang 
for index, c in enumerate(lang, start=1): 
	print ("Language: %s Characters: %s"%(c, characters[index]))

# Printing characters of langtype 
for index, a in enumerate(langtype, start=1): 
	print ("Type: %s Characters: %s"%(a,characters[index+len(lang)])) 
