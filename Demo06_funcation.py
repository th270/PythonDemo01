

"""
    1- 默认值的参数：
        #默认参数
        # n = 2  就是默认参数
        def power(x,n=2):


    2- 可变参数：可以输入0到任意个参数，函数组装成tuple 元组
        #可变参数
        # *numbers
        #N个数求和
        def my_sum(*numbers):

        # 如果调用函数的参数是可变参数，在调用的时候也可以使用可变参数的形式元组调用
        #由于可变参数 其实就是一个tuple 元组，所以传参数时也可以使用一个元组 但是必须加上*
        numbers = [2,5,1,9]
        print(my_sum(*numbers))

    3- 关键字参数： 可以输入0 到任意个含参数名参数，函数内组装成一个dict （字典）
        #关键字参数
        # **kw 关键字参数
        # **kw 是一个dict字典的类型
        def student(name,age,**kw):
            print("name:",name,"age:",age,"others:",kw)
            print(type(kw))
        # 关键字参数
        # 关键字参数调用的时候必须使用键值对的形式传送参数
        # from MyFuncation import student
        # student("Tom",20,sex="male",region="china")

        #由于关键字参数 其实就是一个dict 字典，所以传参数时也可以使用一个字典 但是必须加上**
        # dicts = {"sex" : "male","region":"china"}
        # student("Tom2",22,**dicts)

    4- 命名关键字参数
        # 命名关键字参数
        #  *,city  就是一个必须有一个参数是city,在传入参数的时候就是一个普通的关键字参数（字典）
        def student(name,age,*,city):
            print("name:", name, "age:", age, "city:", city)
            print(type(city))
        #命名关键字参数
        #就是指定名称的参数
        from MyFuncation import student
        student("Jerry",28,city="femail")
    5- 多种参数混合顺序： 默认-可变-命名关键字-关键字
"""

#内置函数
#1- 绝对值
import math

print(abs(-100))

print(dir(math))

print(math.exp(1))

from MyFuncation import  my_abs

print(my_abs(-23))

#查看函数的说明文档
help(my_abs)
print(my_abs.__doc__)
print(abs.__doc__)

#函数出错友好提示
#print(my_abs("ads"))


#函数返回多值
from MyFuncation import getNames
name1,name2 = getNames()
print(name1,name2)
print(type(name1))
names = getNames()
print(type(names),"names =",names)
print(isinstance(names,tuple))


#默认参数
from MyFuncation import power
print(power(2))
print(power(2,-2))

#可变参数
from MyFuncation import my_sum
print(my_sum(4,2,6,3,5))

# 如果调用函数的参数是可变参数，在调用的时候也可以使用可变参数的形式元组调用
#由于可变参数 其实就是一个tuple 元组，所以传参数时也可以使用一个元组 但是必须加上*
numbers = [2,5,1,9]
print(my_sum(*numbers))


# 关键字参数
# 关键字参数调用的时候必须使用键值对的形式传送参数
# from MyFuncation import student
# student("Tom",20,sex="male",region="china")

#由于关键字参数 其实就是一个dict 字典，所以传参数时也可以使用一个字典 但是必须加上**
# dicts = {"sex" : "male","region":"china"}
# student("Tom2",22,**dicts)


#命名关键字参数
#就是指定名称的参数
from MyFuncation import student
student("Jerry",28,city="femail")


# 全局变量与局部变量
# 在局部内使用全局变量，需要使用global
name = "Tom"
def fun():
    global  name
    print("函数内输出全局变量",name)
    name = "Jerry"
    print("name =",name)
fun()
print("函数外输出全局变量",name)


