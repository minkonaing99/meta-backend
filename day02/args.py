def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4,5,6,7,8))


# def sum_of(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum

# print(sum_of(4,5,6,7,8))

def sum_of(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return sum

print(sum_of(coffee = 3.14, cake = 10.33))