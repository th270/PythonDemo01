

def addNum(x,y):
    return abs(x) + abs(y)

print(addNum(100,-220))
print(addNum(100.9,-220))


"""
    高阶函数：
        1- 一个函数名作为另一个函数的实参
    
    
"""

def power(x,count = 2):
    return x**count

def addNum(x,y,fun=abs):
    return fun(x) + fun(y)

print(addNum(100.2,-200.9,abs))
print(addNum(100.2,-200.9,round))
print(addNum(100.2,-200.9))
print(addNum(2,3,power))


## 内置高阶函数 map(func,lst)
## 讲列表lst中的所有数据做func计算后再返回一个迭代器
print("*"*100)
list1 = [1,2,3,4,5]

def func(x):
    return x**2

result = map(func,list1)
print(result)
print(type(result))
for i in result:
    print(i , end=" ")
print()


## 内置高阶函数reduce(func,lst)
## 其中func必须有两个参数。
## 每次func 计算的结果和序列的下一个元素累积计算
print("*"*100)
import  functools
list1 = ["aaa"]
def fucReduce(a,b):
    return a + " " + b

result = functools.reduce(fucReduce,list1)
print(result)


## 内置高阶函数filter(func ,lst)
## 用于过滤列表，过滤掉不符合条件的元素
## 返回一个filter对象。
## 如果要转换成一个列表，可以使用list()来转换
print("*"*100)
list1 = [1,2,3,4,5,6,7,8,9,10]
def funcFilter(x):
    return x % 2 == 0

result = filter(funcFilter,list1)
print(type(result))
print(result)
print(list(result))




