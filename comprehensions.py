data = [2,3,5,7,11,13,17,19,23,29,31]


data = [x+3 for x in data]
print(data)

new_data = [x+2 for x in data]
print(new_data)

even = [x for x in data if x%2 == 0]
print(even)

odd = [x+1 for x in data if x%2 ==0]
print(odd)


usingRange = {x:x*2 for x in range(12)}
print(usingRange)

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

numDict = {x:x**2 for x in number}
print(numDict)

months_dict = {key:value for (key,value) in zip(number, months)}
print(months_dict)

emails = [" A@x.com ", "", "b@y.com"]
clean = [e.strip().lower() for e in emails if e.strip()]
print(clean)

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")
    
    
    
z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)