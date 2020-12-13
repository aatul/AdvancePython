"""
Nested Functions:

Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. That is using closures, one could make functions to create multiply_with(), multiply_with_2(), multiply_with_3(), multiply_with_4() or multiply_with_5() functions using closures.
"""

def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiply_with = multiplier_of(5)
print(multiply_with(9))