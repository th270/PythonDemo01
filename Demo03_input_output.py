import keyword

name = input("请输入您的姓名:")
print("您的名字叫",name)

#如果在使用print 的时候不想换行 可以使用 end=""
print("a" ,end=" ")
print("b" ,end=" ")
print("c" ,end="\n")

print("a" ,end="-")
print("b" ,end="-")
print("c" ,end="\n")


a = input("请输入正方形的长")
b = int(a)
s = b ** 2  # b*b
print("正方形的边长 =",b,"\n面积s ==",s)

#输出 python 的关键字
print(keyword.kwlist)

