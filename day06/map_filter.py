menu = ["expresso", "mocha", "latte", "cappachino", "cortado", "americano"]

# map(function, ariticle)

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee
    
    
map_coffee = map(find_coffee, menu)
print(list(map_coffee))

filter_coffee = filter(find_coffee, menu)
print(list(filter_coffee))

# maps take all objects in a list and applies a function
# filter do the same, but take the results and creates a new list with only the true values