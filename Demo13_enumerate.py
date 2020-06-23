
list1 = ["a","b","c"]

for i in enumerate(list1):
    print(i)

for i in enumerate(list1,1):
    print(i)

for i,element in enumerate(list1,1):
    print(f"{i} = {element}")



