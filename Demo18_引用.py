
a = 100
b = a
print(f"a = {a}")
print(f"b = {b}")
print(f"a id = {id(a)}")
print(f"b id = {id(b)}")
b = 200
print(f"a = {a}")
print(f"b = {b}")
print(f"a id = {id(a)}")
print(f"b id = {id(b)}")


#列表
l1 = [100,200,300]
l2 = l1
print(f"l1 = {l1}")
print(f"l2 = {l2}")

print(f"l1 id = {id(l1)}")
print(f"l2 id = {id(l2)}")

l1[1] = 400

print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(f"l1 id = {id(l1)}")
print(f"l2 id = {id(l2)}")





