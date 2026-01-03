# type of errors
# syntax errors
# exceptions

# Known errors that need to be handled are exceptions.

# exception handling

def divide_by (a,b):
    return a / b

try:
    ans = divide_by(40,0)
except ZeroDivisionError as e:
    print("Somethign went wrong", e)
except Exception as e:
    print(e)

