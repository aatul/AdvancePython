# Generating list without list comprehension
# Define a list
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

# Define an empty list for output
list2 = []

# Generate list using for loop, regular/general way
for x in list1:
    if x%2 == 0:
        list2.append(x)
print(list2)

# Generating list with list comprehension
list3 = [x for x in list1 if x%2 == 0]
print(list3)

# Generate a list of squares from 0-10
list4 = [x**2 for x in range(10)]
print(list4)

# Generate a list of 2^x
list5 = [2**x for x in range(10)]
print(list5)

