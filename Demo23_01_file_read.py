

"""
file 读：
    1- read(size) 用于从文件读取指定的字节数，如果未给定或为负则读取所有。
        size -- 从文件中读取的字节数。

    2- readline(size) 方法用于从文件读取整行，包括 "\n" 字符。
        如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
        size -- 从文件中读取的字节数。
"""

## read(size)
f = open("test.txt","r")
print(f.name)
print(f.read())
f.seek(0,0)
print(f.read(20))
f.flush()
f.close()
""" 
结果：
test.txt
1- Hello world!
2- Hello world!
3- Hello world!
4- Hello world!
5- Hello world!
1- Hello world!
2- H
"""


## readline()
print("*"*100)
f = open("test.txt","r")
con = f.readline()
print(type(con))
print(con)
f.flush()
f.seek(0,0)
print(f.readline(10))
f.flush()
f.seek(0,0)
f.close()
"""
结果：
    <class 'str'>
    1- Hello world!
    1- Hello w

"""


"""
1- r+ w+ a+ 区别：
2- 文件指针对数据读取的影响
"""
### r+ ：
### 1- 没有这个文件是打开会报错；
### 2- 文件指针在文件开头；所以能读取文件所有数据；
fr = open("test1.txt","r+")
f = open("test.txt","r+")
print(f.read())

### w+ :
### 1- 没有该文件就会新建这个文件；
### 2- 文件指针在文件的开头，但是文件里面原来的内容会被覆盖（清空）
f = open("test1.txt","w+")
f = open("test.txt","w+")
print(f.read())

### a+ :
### 1- 没有该文件就会新建这个文件；
### 2- 文件指针在文件的结尾，所有无法读取数据（文件指针后面没有数据）
f = open("test.txt","a+")
print(f.read())

f.close()


