# Starter code
items = [1,2,3,4,5]

try:
    item = items[6]
except Exception as e:
    print(e)


# Starter code
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
except Exception as e:
    print(e)

# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except Exception as e:
    print(e)
