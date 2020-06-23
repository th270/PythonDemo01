


import  os
fileList = os.listdir()
# print(fileList)


for fileName in fileList:
    # newFileName = "Python_"+fileName
    # #newFileName = fileName[len("Python_"):]
    # os.rename(fileName,newFileName)

    if fileName.__contains__("Python_"):
        newFileName = fileName[len("Python_"):]
        os.rename(fileName, newFileName)


