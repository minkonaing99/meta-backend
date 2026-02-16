
#Exercise 1: Squares of even numbers
nums = [1,2,3,4,5,6,7,8,9,10]
square = [x**2 for x in nums if x%2 == 0]
print (square)

#Exercise 2: Price lookup dict
items = [
  {"sku": "A1", "price": 120},
  {"sku": "B2", "price": 75},
  {"sku": "C3", "price": 310},
]

look_up = {item["sku"]:item["price"] for item in items}
print(look_up)

#Exercise 3: Reverse a dict (careful with duplicates)
d = {"th": "Thailand", "jp": "Japan", "kr": "Korea"}
reverse = {value:key for (key,value) in d.items()}
print(reverse)


#Exercise 4: Zip + filter
names = ["ann", "bob", "chris", "dana"]
scores = [50, 82, 91, 40]

result = {key:value for (key,value) in zip(names, scores) if value >= 60}
print (dict(result))


#Exercise 5: Generator vs list (memory-safe)
nums = range(10_000_000)
total = sum(x for x in nums)
print(total)