"""
nonlocal keyword:

Without the nonlocal keyword, the output would be "3 9", however, with its usage, we get "3 3", that is the value of the "number" variable gets modified.

Now, how about we return the function object rather than calling the nested function within. (Remember that even functions are objects in Python.)
"""

def print_number(number):
    def printer():
        # Here we are using the nonlocal keyword
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_number(9)