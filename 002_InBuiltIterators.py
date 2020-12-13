# Sample built-in iterators 

# Iterating over a list 
print("List Iteration") 
l = ["Java", "Android", "Python"] 
for i in l: 
	print(i) 
	
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("Java", "Android", "Python") 
for i in t: 
	print(i) 
	
# Iterating over a String 
print("\nString Iteration")	 
s = "Python"
for i in s : 
	print(i) 
	
# Iterating over dictionary 
print("\nDictionary Iteration") 
d = dict() 
d['pqr'] = 123
d['abc'] = 345
for i in d : 
	print("%s %d" %(i, d[i])) 
