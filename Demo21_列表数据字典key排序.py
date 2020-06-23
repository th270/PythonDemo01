
##使用lambda表达式对列表中的字典元素排序
students = [
    {"name":"Tom4","age":24},
    {"name":"Tom3","age":23},
    {"name":"Tom2","age":22},
    {"name":"Tom1","age":21}
]
# students.sort(key=lambda x : x["name"])
# print(students)
# students.sort(key=lambda x : x["name"],reverse=True)
# print(students)
# students.sort(key=lambda x : x["age"])
# print(students)
# students.sort(key=lambda x : x["age"],reverse=True)
# print(students)


students.sort(key = lambda x:x["name"])
print(students)


students.sort(key = lambda x:x["name"],reverse=True)
print(students)


students.sort(key = lambda  x : x["age"],reverse=False)
print(students)

students.sort(key = lambda x : x["age"],reverse=True)


