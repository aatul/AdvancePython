"""
Enumerate:

Enumerate is built-in python function that takes input as iterator, list etc and returns a tuple containing index and data at that index in the iterator sequence.

For example, enumerate(lang), returns a iterator that will return (0, lang[0]), (1, lang[1]), (2, lang[2]), and so on.
"""

# Define a list
lang = ["English", "Hindi", "Marathi", "Arabic"] 

# Accessing items using enumerate() 
for i, x in enumerate(lang): 
	print(x) 

# Accessing items and indexes enumerate() 
for x in enumerate(lang): 
	print(x[0], x[1]) 

# Printing return value of enumerate() 
print(enumerate(lang))

# Using start in enumerate
# Enumerate takes parameter start which is default set to zero. We can change this parameter to any value we like. In the below code we have used start as 11.
for x in enumerate(lang, start=11): 
	print(x[0], x[1]) 

