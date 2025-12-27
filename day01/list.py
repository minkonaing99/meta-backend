list1 = [1,2,3,4]
list2 = ["a", "b", 'c']
list3 = ['hello', 1, True, 46.33]
list4 = [1,2,3, [1,2,3]]

print(*list1)

list1.insert(len(list1), 6)

list1.append(7)
list1.extend([8,9])

list1.pop(4)
del list1[2]
print(list1)

for i in list1:
    print('Value', i)
    
    