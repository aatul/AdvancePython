"""
Generator Expression:

Python allows writing generator expressions to create anonymous generator functions.

This procedure is similar to a lambda function creating an anonymous function.

The syntax of a generator expression is the same as of list comprehension in Python. However, the former uses the round parentheses instead of square brackets.
"""

# Define a list
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

# Find square using the list comprehension
list2 = [x**2 for x in list1 if x%2 == 0]
print(list2)

# Use generator expression to calculate the square 
gen_exp = (x**2 for x in list1 if x%2 == 0)
for x in gen_exp:
    print(x,end=' ')


"""
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
"""