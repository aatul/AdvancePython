"""
The reverse of the iterators from zip function is known as unzipping using '*' operator.

Use of enumerate function and zip function helps to achieve an effective extension of iteration logic in python and solves many more sub-problems of a huge task or problem.
"""

# Let's unzip (reverse of zip) using * with zip function 

# Unzip lists 
l1,l2 = zip(*[('English', 'Business Language'), 
			('Hindi', 'Native Language'), 
			('Marathi', 'Mother Tounge') 
		]) 

# Printing unzipped lists	 
print(l1) 
print(l2) 
