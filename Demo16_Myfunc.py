
##默认参数
def power(x,n=2):
    """
    求 x 的 n 次方
    :param x:  底数x
    :param n:  指数 n
    :return:  x ** n
    """
    if not isinstance(x,(int,float)):
        raise TypeError ("参数x只能输入int 或者 float")
    if not isinstance(n,(int,float)):
        raise TypeError ("参数n只能输入int 或者 float")
    return x**n


#可变参数
def getSum(*nums):
    sum = 0
    print(type(nums))
    for i in nums:
        sum += i
    return sum


#关键字参数
def Student(name,age,**kw):
    print(type(kw))
    print(f"name = {name},age = {age},orthers = {kw}")

def userInfo(name ,age, gender):
    print(f"name = {name},age = {age},gender = {gender}")


#命名关键参数
def Teacher(name,age,*,city):
    print(type(city))
    print(f"name = {name},age = {age},city = {city}")



def printLine(count = 20):
    """

    :return:
    """
    print("-"*count)

def printLines(num,count = 20):
    """

    :param num:
    :return:
    """
    if not isinstance(num,(int)):
        raise TypeError("参数num 必须是int类型")
    else:
        for i in range(num):
            printLine(count)
