
#空方法
def fun():
    pass


def my_abs(number):
    '''
    自定义abs
    :param number:  int 或者 float
    :return: abs 绝对值
    '''
    #参数判断  #函数出错友好提示
    if not isinstance(number,(int,float)):
        raise TypeError("只能输入int 和 float 类型")
    if number >= 0:
        return number
    else:
        return -number



def getNames():
    '''
    返回多个值
    :return:  返回多个值时返回的事一个tuple元组
    '''
    return "Tom1","Tom2"



#默认参数
# n = 2  就是默认参数
def power(x,n=2):
    '''
    x 的 n 次方
    :param x:  底数
    :param n:  指数
    :return:  x的n次方后的值
    '''
    return x**n

#可变参数
# *numbers
#N个数求和
def my_sum(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum += i
    return sum


#关键字参数
#**kw 关键字参数
#**kw 是一个dict字典的类型
# def student(name,age,**kw):
#     print("name:",name,"age:",age,"others:",kw)
#     print(type(kw))

# 命名关键字参数
#  *,city  就是一个必须有一个参数是city,在传入参数的时候就是一个普通的关键字参数（字典）
def student(name,age,*,city):
    print("name:", name, "age:", age, "city:", city)
    print(type(city))

