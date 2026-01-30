

data = ["1", "2", "3", "4"]

numbers = map(int, data)

print(list(numbers))

n = [1,2,3,4,5]
plusOne = lambda n: n+1
result = map(plusOne, n)
print(list(result))