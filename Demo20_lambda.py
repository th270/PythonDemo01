
"""
语法格式：
    lambda 参数列表: 表达式
lambda 特点：
    1- lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
    2- lambda表达式能接收任何数量的参数但只能返回一个表达式的值
"""


fn = lambda :100
print(fn)
print(fn())
print(lambda :200)



fn1 = lambda a,b:a+b
print(fn1(100,200))




"""
Lambda 表达式 又叫 匿名函数
语法格式：
    lambda 参数列表: 表达式
lambda 特点：
    1- lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
    2- lambda表达式能接收任何数量的参数但只能返回一个表达式的值
    3- 一个函数只有一行代码一个返回值 就可以简写成一个lambda 表达式

lambda的参数形式：
    1- 无参数
        fn1 = lambda:100
    2- 一个参数
    3- 默认参数
    4- 可变参数
    5- 关键字参数
    
"""

## 无参数
fn1 = lambda : 100
print(fn1())

## 一个参数
fn2 = lambda  str : str
print(fn2("Hello world!"))


## 默认参数（缺省参数）
fun3 = lambda x,n = 2 : x**n

print(fun3(3))
print(fun3(3,4))

## 可变参数
fun4 = lambda *args : args
print(type(fun4("str1","str2","str3")))
print(fun4("str1","str2","str3"))

## 关键字参数
fun5 = lambda  **kwargs : kwargs
print(type(fun5(name="Tom" , age = 20 , gender = "男")))
print(fun5(name="Tom" , age = 20 , gender = "男"))



#Python 三目运算符
num = 20 if 20 > 50 else 50
print(f"num = {num}") ## num = 50

## 带判断的lambda
fun6 = lambda x,y : x if x > y else y
print(fun6(2000,3990)) ## 3990





