def make_coffee(water, beans):
    return f"Coffee mad with {water}ml water and {beans}g beans"

americano = make_coffee(12,3)
print(americano)

def greet(name):
    return f"Hello {name}"
result = greet("Thomas")
print(result)

def create_user(name, role="viewer", is_active=True):
    return {"name" : name, "role":role,"is_active": is_active}

print(create_user("Thomas"))
print(create_user("Bob", "Admin"))
print(create_user("Aston", "admin", False))



def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags

print(add_tag("python"))
print(add_tag("django"))



def total(*args):
    return sum(args)
print(total(10, 20,30))
print(total(5,5))



#layer 3

def double(n):
    n = n * 2
    return n

x = 10
y = double(x)
print(y)

def add_item(items, item):
    copy_items = items.copy()
    copy_items.append(item)
    return copy_items
cart = ["apple", "banana"]
print(add_item(cart, "cherry"))

import copy
original = {"user":{"name":"Thomas", "tags":["admin"]}}
clone = copy.deepcopy(original)
clone["user"]["tags"].append("editor")
print(original)
print(clone)


def get_user(id):
    return {"id":id, "name":"Thomas", "role":"admin"}
user = get_user(1)
print(user["name"])

def get_tags(text):
    return text.lower().split()
print(get_tags("Python Django REST"))

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3,1,3,1,5,9])
print(low, high)