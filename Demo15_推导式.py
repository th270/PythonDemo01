
"""
    列表
    字典
    集合
    只有这三种数据类型才有推导式
"""


####列表推导式 ： 用一个表达式创建一个有规律的列表或控制一个有规律的列表

list1 = []

i = 0
while i < 10:
    list1.append(i)
    i += 1

print(list1)

list1.clear()
for i in range(0,10):
    list1.append(i)
print(list1)

# 列表推导式
list2 = list(i for i in range(10))
print(f"列表推导式 list2 = {list2}")

list3 = [i for i in range(0,10)]
print(f"list3 = {list3}")

####带if 的列表推导式

list4 = list(i for i in range(0,10,2))
print(f"list4 = {list4}")

list5 = [i for i in range(10) if 0 == i % 2 ]
print(f"list5 = {list5}")

##多个for 循环 列表推导式
list6 = []
for i in range(1,3):
    for j in range(3):
        # t = (i,j)
        # list6.append(t)
        list6.append((i,j))

print(list6)

list7 = [(i,j) for i in range(1,3) for j in range(3)]
print(f"list7 = {list7}")

list8 = list((i,j) for i in range(1,3) for j in range(3))
print(f"list8 = {list8}")



####字典推导式

d1 = {i : i**2 for i in range(1,5)}
print(f"d1 = {d1}")

d2 = dict({i : i**3 for i in range(1,5)})
print(f"d2 = {d2}")

list1 = ["name","age","gender"]
list2 = ["Tom",28,"man"]

d3 = dict({list1[i]:list2[i] for i in range(len(list2))})
print(f"d3 == {d3}")


#提取字典中满足条件的元素
counts = {"MBP":268,"HP":125,"DELL":201,"LENOVO":200,"ACER":99}
computers = {key:value for key, value in counts.items() if value >= 200}
print(f"computers = {computers}")


###集合推导式
l1 = [1,2,1]
set1 = set(i ** 2 for i in l1)
print(f"set1 = {set1}")


list1 = list((i,j) for i in range(1,3) for j in range(3))
print(list1)


dict1 = {i:i**3 for i in range(5)}
print(dict1)

list1 = ["name","age","gender"]
list2 = ["Tom",28,"man"]
d = {list1[i]:list2[i] for i in range(len(list1))}
print(d)









