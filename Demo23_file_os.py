
import  os
import shutil
#
# 1 rename 重命名
# os.rename("test.txt","test100.txt")
# os.rename("test100.txt","test.txt")
#
#
# # 2- 删除文件 remove
# print(os.path.isfile("test.txt"))
# fileList = os.listdir(".")
# print(fileList)
# for file in fileList:
#     if(file.__contains__("备份")):
#         os.remove(file)
#
# # 3- 创建文件夹
# if os.path.exists("aa"):
#     print("该目录或文件已经存在")
#     shutil.rmtree("aa")
#
# os.mkdir("aa")
# fd = open("aa/test.txt","w")
# print(type(fd))
# fd.close()

# 4- 获取当前路径 getcwd()
# print(os.getcwd())

# 5- 改变当前默认目录 chdir()
# os.chdir("aa")
# print(os.getcwd())
# os.mkdir("bb")
# os.chdir("bb")
# print(os.getcwd())
# f = open("test_1000.txt","w")
# f.close()
# os.chdir("../../")
# print(os.getcwd())

# 5- 获取当前目录下的所有文件
# def printDir(dirName,count = 0):
#     files = os.listdir(dirName)
#     # print(type(files))
#     for fileName in files:
#         print("\t"*count,fileName)
#         isDir = os.path.isdir(fileName)
#         if isDir:
#             os.chdir(fileName)
#             printDir(fileName,count + 1)
#
# #printDir("./",0)
# # print(os.path.isdir("StudentSystem/src"))
# # os.chdir("StudentSystem")
# # print(os.getcwd())
# # print(os.path.isdir("src"))
#
# printDir("StudentSystem")
#
# print(os.path.isdir("StudentSystem/src"))
#
# print(os.listdir("StudentSystem/src"))


# 6- 重命名 rename
# os.rename("bb","bbbb")


