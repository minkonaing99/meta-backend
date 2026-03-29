# str, int, float, bool, list, tuple, dict, set, None

age = 25
score = -10

price = 19.99

is_logged_in = True
has_permission : bool= False


result = None

name :str = "thomas"
greeting = "  hello world    "
multiline = """
line one
line two
"""
print(name)

name = "T" + name[1:]
print(name)


print(greeting.strip())
print("hello {}".format("Thomas"))
print(f"Hello {name}")
print(greeting.replace(" ", '/'))
print(greeting.strip().split(" "))
print(greeting.startswith("he")) #result bool

fruits = ["apple" , "banana" , "cherry"]
mixed = [1, "hello", True, None]

fruits[0] = "mongo"
fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.remove("banana")
fruits.pop()
fruits.pop(0)
len(fruits)

print(fruits)
print(fruits.reverse())
print(fruits.sort())

squares = []
for n in range(1,5):
    squares.append(n**2)

squares = [n ** 2 for n in range(1,5)]
print(squares)

evens = [n for n in range(10) if n%2 == 0]

tuple_coordinate = (123, 456) # unchanged, ordered

# dict
user = {
    "name": "thomas",
    "age" : 25,
    "is_active" : True,
}

print(user["name"])
user["email"] = "123@gmail.com"
print(user.get("email"))
print(user.get("email", "N/A"))
user["age"] = 27
del user["is_active"]
print(user.keys())
print(user.values())
print(user.items())

square = {k:"thomas: "+str(v) for k,v in user.items()}
print(square)

# set
tags = {"python", "django", "web"}
# use sets when uniqueness matters and order doesn't

tags.add("api")
tags.remove("web")
len(tags)
print(tags)

nums = [1,2,2,3,3,3]
unique = list(set(nums))
print(unique)