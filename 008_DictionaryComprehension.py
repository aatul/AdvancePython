# Define a list
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

# Define an empty Dictionary for output
dict1 = {}

# Generating dictionary using for loop
# Even numbers (keys) and their respective square (values)
for x in list1:
    if x%2 == 0:
        dict1[x] = x**2

# Driver Code
print(dict1)

# Generating dictionary using comprehension
dict2 = {x:x**2 for x in list1 if x%2 == 0}
print(dict2)

