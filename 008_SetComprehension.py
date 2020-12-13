# Define a list
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

# Define an empty Set for output
set1 = set()

# Generate set using for loop, regular/general way
for x in list1:
    if x%2 == 0:
        set1.add(x)

print(set1)

# Generating set with list comprehension
set2 = {x for x in list1 if x%2 == 0}
print(set2)