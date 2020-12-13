O

# An iterable user defined type 
class Test: 

	# Cosntructor 
	def __init__(self, limit): 
		self.limit = limit 

	# Called when iteration is initialized 
	def __iter__(self): 
		self.x = 10
		return self

	# To move to next element. In older versions of Python, we should replace __next__ with next
	def __next__(self): 

		# Store current value ofx 
		x = self.x 

		# Stop iteration if limit is reached 
		if x > self.limit: 
			raise StopIteration 

		# Else increment and return old value 
		self.x = x + 1
		return x 

# Prints numbers from 10 to 15 
for i in Test(15): 
	print(i) 

# Prints nothing 
for i in Test(5): 
	print(i) 
