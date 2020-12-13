# Define a list
list1 = [1,2,3,4,5,6,7,8,9,10]
print("Original list1:")
print(list1)

# Print elements of a range using Slice operation 
sliced_list = list1[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(sliced_list) 
  
# Print elements from a pre-defined point to end 
sliced_list = list1[5:] 
print("\nElements sliced from 5th "
      "element till the end: ") 
print(sliced_list) 
  
# Printing elements from beginning till end 
sliced_list = list1[:] 
print("\nPrinting all elements using slice operation: ") 
print(sliced_list) 

# Print elements from beginning to a pre-defined point using Slice 
sliced_list = list1[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(sliced_list) 
  
# Print elements of a range using negative index list1 slicing 
sliced_list = list1[-6:-1] 
print("\nElements sliced from index -6 to -1") 
print(sliced_list) 
  
# Printing elements in reverse using Slice operation 
sliced_list = list1[::-1] 
print("\nPrinting list1 in reverse: ") 
print(sliced_list) 