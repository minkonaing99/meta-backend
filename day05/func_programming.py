coffees = ['espresso', 'latte', 'cappuccino', 'macchiato', 'americano', 'decaf']

print(sorted(coffees))

def reverse(str):
    return str[::-1]
reversed_coffees = map(reverse, coffees)

for x in reversed_coffees:
    print(x)