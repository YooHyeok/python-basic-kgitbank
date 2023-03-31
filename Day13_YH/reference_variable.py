
a = 3
b = a
print(a, b)

a = 5
print(a, b)

list1 = [1,2,3]
list2 = list1
print("list1:", list1)
print("list2:", list2)

list1[0] = 6
list1[2] = 9
print("list1:", list1)
print("list2:", list2)
print("list1의 주소값:", hex(id(list1)))
print("list2의 주소값:", hex(id(list2)))












































