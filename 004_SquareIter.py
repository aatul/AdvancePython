Squares = (1, 4, 9, 16, 25)
sq = iter(Squares)
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))

"""
The number of times you call next, will print next element those many time.

If next is called more than the number of elements then will throw StopIteration error
"""