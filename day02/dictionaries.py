# dict_a = {
#     "key":"value" ,
#     1:"coffee",
#     2:"tea"
# }

# print(dict_a["key"])

# dict_a[2] =  "mint tea"

# print(dict_a)


my_d = {1:'Test', "name": "Jim"}
my_d[2] = "Test2"
print(my_d)


for key, value in my_d.items():
    print(str(key) + " : " + value)
    
    
    
my_list = [1, 2, 3, 4, 5, 6]
my_list[0] = 0
print(my_list)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.intersection(set_b))