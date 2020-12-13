"""
zip function (Both iterators to be used in single looping construct):

This function is helpful to combine similar type iterators(list-list or dict-dict etc,) data items at ith position.

It uses the shortest length of these input iterators.Other items of larger length iterators are skipped. In case of empty iterators, it returns No output.

For example, the use of zip for two lists (iterators) helped to combine a single car and its required accessory.
"""

# Define Two separate lists 
lang = ["English", "Hindi", "Marathi", "Arabic"] 
langtype = ["Business Language", "Native Language", "Mother Tounge"]

# Combining lists and printing 
for l, lt in zip(lang, langtype): 
	print("Language: %s, Language Type: %s"%(l, lt))
