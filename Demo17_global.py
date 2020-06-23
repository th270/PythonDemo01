
a = 100

def testA():
    print(a)

def testB():
    global  a  # 在方法中修改全局变量的值
    a = 200
    print(a)

print(a)
testA()
testB()
print(a)


x = 1000
y = 2000
x,y = y,x
print(f"x = {x}")
print(f"y = {y}")

