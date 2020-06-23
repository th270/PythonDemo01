
dict1 = {"name":"Tom","age":20,"gender":"男"}

#新增元素 或者 修改元素
dict1["id"] = "420582199109056691"
print(dict1)
dict1["name"] = "Rose"
print(dict1)

#删除 字典 或指定的键值对（如果key存在就删除，如果不存在就报错）  del
#del dict1
#del(dict1)
# del dict1["names"]
del dict1['name']
print(dict1)



#清空字典 clear
dict1.clear()
print(dict1)




dict1 = {"name":"Tom","age":20,"gender":"男"}
dict1["age"] = 22
print(dict1)




"""
    get()
    keys()
    values()
    items()
"""
dict1 = {"name":"Tom","age":20,"gender":"男"}
#get()
print(dict1.get("name"))
print(dict1.get("names"))
print(dict1.get("names","Lily"))
#keys
print(dict1.keys())
for key in dict1.keys():
    print(key , ":" , dict1.get(key))
keys = dict1.keys()
if "name" in keys:
    print("name = ",dict1.get("name"))


#values
print(dict1.values())
for value in dict1.values():
    print(value)



#items
items = dict1.items()
print(items)
print(type(items))
for item in items:
    print(item)
    print(type(item))
    print(item[0],"=",item[1])

print(len(items))
newDict = dict(items)
print(newDict)


for key , value in dict1.items():
    print(f"{key} = {value}")

lists = [("name","Tom"),("age",20),("gender","男")]
dict2 = dict(lists)
print(f"new dict2 = {dict2}")


# 两个dict 叠加
dict1 = {"name":"Tom","age":20,"gender":"男"}
dict2 = {"id":"4205811991"}
dict1.update(dict2)
print(dict1)




mydict = {}
if 0 == len(mydict):
    print("myDict is None")






