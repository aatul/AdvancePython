"""
PARTIAL FUNCTIONS

Partial functions allow us to fix a certain number of arguments of a function and generate a new function.
"""

from functools import partial 

# A normal function 
def my_function(a, b, c, x): 
	return 1000*a + 100*b + 10*c + x 

# A partial function that calls my_function with a as 1, b as 2 and c as 3. 
test = partial(my_function, 1, 2, 3) 

# Driver Code: Calling test() 
print(test(4)) 

"""
In this example, we have pre-filled our function with some constant values of a, b and c. And test() just takes a single argument i.e. the variable x.
"""