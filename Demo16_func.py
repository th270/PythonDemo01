
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



###默认参数
from Demo16_Myfunc  import  power
print(power(2,3))
print(f"默认参数函数调用power：{power(2)}")
# power("sdf")


###可变参数
from Demo16_Myfunc import getSum
list1 = [10,20,30,40]
t1 = (10,20,30,40)
print(f"可变参数：{getSum(*(10,20,30,40))}")
print(f"可变参数：{getSum(*[10,20,30,40])}")
print(f"可变参数：{getSum(*list1)}")
print(f"可变参数：{getSum(*t1)}")
print(f"可变参数：{getSum(20,20,20,20,20,20)}")

###关键字参数
from Demo16_Myfunc import Student
dict1 = {"gender":"man","id":"110"}
Student("Tom",29,**{"gender":"man","id":"110"})
Student("Jerry",30,**dict1)
Student("Rose",31,gender="man",id=111110000)

from Demo16_Myfunc import userInfo
userInfo("Rose1111",20,"woman")
userInfo("Rose222",age = 21,gender = "woman")
userInfo("Rose333",gender = "woman",age = 22)


###命名关键字参数
from Demo16_Myfunc import Teacher
Teacher("Rose",24,city="wuhan")


help(power)


from Demo16_Myfunc import printLines
# printLines(5)
printLines(5,50)


