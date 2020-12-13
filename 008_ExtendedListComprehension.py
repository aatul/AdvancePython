# Generating list without list comprehension
# Define a extended list or nested list
list1 = [[1,2,3],[4,5,6],[7,8,9]]
print(list1)

# Define an empty list for output
list2 = []

# Generate nested list using for loop, regular/general way
for x in range(3):
    # Append empty nested list to main list
    list2.append([])
    for y in range(3):
        list2[x].append(y)

print(list2)

# Generating nested list with list comprehension
list3 = [[y for y in range(3)] for x in range(3)] 
print(list3)

# Convert the nested list to a normal list using for loop
list4 = []
for x in list1:
    for y in x:
        list4.append(y)
print(list4)

# Convert the nested list to a normal list using nested list comprehension
list5 = [y for x in list1 for y in x]
print(list5)
