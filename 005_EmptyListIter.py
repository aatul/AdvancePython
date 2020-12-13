"""
Iterator on Empty List

If we try to iterate over empty list, it will throw StopIteration Error
"""
EmptyList = []
listelement = iter(EmptyList)
print(next(listelement))
print(next(listelement))