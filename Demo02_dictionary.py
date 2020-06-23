

#字典 dictionary
'''
    1- 无序集合
    2- 键值对
    3- 使用{}
    4- 字典的key 必须是不可变对象： 数字、字符串

    有点： 查找 插入 快
    缺点： 占用内存
'''

#list 实现：
names = ["Tom1","Tom2","Tom3","Tom4"]
scores = [91,92,93,94]
print(names)
print(scores)

#字典实现
d = {"Tom1":91,
     "Tom2":92,
     "Tom3":93,
     "Tom4":94}
print(d)

#检索 使用 []
print("Tom2 :" ,d["Tom2"])

#添加
d["Tom5"] = 46
print(d)

#替换
d["Tom2"] = 100
print(d)

#判断key 是否在字典中？
print("Tom3" in d)

#如果这个key 不存在 报错： KeyError: 'Tom'
#print(d["Tom"])
#可以使用 字典中的get 方法  当key不存在是返回默认值 -1
print(d.get("Tom" ,-1))



