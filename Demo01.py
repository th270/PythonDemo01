
print("hello world Tom")

a = 1.29e8
print(type(a))

print(3<2)

print(5>2 or 3<2)

print(not True)

print(not 1<1)

print(3>2 and 1<3)

n = None
print(type(n))
print(n)

print(1==2)


x = 10
x = x+2
print("x == " ,x)

PI = 3.1415926

#//float运算
print(10/3)
#//取整
print(10//3)
print(10%3)

#指数 3的平方
print(3**2)

#指数 3的3次方
print(3**3)

print(2**-1)


#字符串
str1 = 'this is string'
str2 = "hello I'm python"
str3 ='hello I\'m python'
str4 =r'hello I\'m python'
print(str1)
print(str2)
print(str3)
print(str4)

#拼接1 短字符串
str5 = "北京" + "你好！"
print(str5)

#拼接2 长（文本）拼接  效率非常高
list_str=["ni","hao","bei","jing"]
str6 = "".join(list_str)
str7 = " ".join(list_str)
print(str6)
print(str7)

#拼接3 format 方式拼接字符串
str8 = "我喜欢{}，因为我需要{}"
str9 = str8.format("python","学习")
print(str8)
print(str9)

#下标取字符
str10 = "abcdefg"
print(str10[0])
print(str10[1])
print(str10[2])
print(str10[3])
print(str10[4])
print(str10[5])
print(str10[6])

#切片
str11 = "abcdefg"
#取abc
print(str11[0:3])
print(str11[:3])
#取cdef
print(str11[2:6])

#取defg
print(str11[3:7])
print(str11[3:])

#取def
print(str11[3:6])
print(str11[3:-1])

#步长  取aceg
print(str11[::2])

#步长  字符串反转
print(str11[::-1])

#字符串替换
print(str11.replace("cd","你好"))

#字符串查找
print(str11.find("f"))
print(str11.find("i"))
print(str11.index("d"))

#字符串 个数
print(str11.count("d"))

str11 = '小红，小白，小李，小花'
list_str = str11.split("，")
print(list_str)
print(type(list_str))
print(list_str[0])
print(str11)


#list 有序集合

classmates = ['Tom',"Jerry","Lisa","Ting"]
print(classmates)
print(type(classmates))
print(len(classmates))
print(classmates[1])

#最后一个元素
print(classmates[-1])
#添加
classmates.append("Pybee")
print(classmates)
#插入
classmates.insert(1,"Long")
print(classmates)
#删除
classmates.pop()
print(classmates)
classmates.pop(3)
print(classmates)
#替换
classmates[1]="Lisa"
print(classmates)

#嵌套
lists=["Tom1","Tom2",["Jerry1","Jerry2","Jerry3"],"Tom3"]
print(lists)
print(len(lists))
print(len(lists[2]))

#List 相加["Tom1","Tom2","Tom3","Tom4"]
list1=["Tom1","Tom2"]
list2=["Tom3","Tom4"]
list3 = list1 + list2
print(list3)

#list 相乘 ["Tom1","Tom2","Tom1","Tom2","Tom1","Tom2"]
list4 = list1*3
print(list4)

#元组 tuple
'''
    1- 元组中的元素不能修改
'''
t = ("a","b","c")
print(t)
#t[1]="b"  元组是不能修改的所有报错：  'set' object does not support item assignment
#print(t)

# 注意： 当元组只有一个元素的时候 必须写成t(1,)
t=(1)
print(type(t))  #<class 'int'>

t=(1,)
print(type(t)) #<class 'tuple'>

#元组中的嵌套的引用型里面的内容可以修改
l= ["A","B","C"]
t = ("a","b","c",l)
print(t)
t[3][2]="D"
print(t)

#但是引用型元素本身不能修改
l1 = ["A","B","C"]
#t[3] = l1 # 报错：'tuple' object does not support item assignment
print(t)


