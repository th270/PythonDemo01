#
# nameList = ["Tom","Lily","Rose"]
# print(nameList)
# for name in nameList:
#
#     print(name)
#
# count = len(nameList)
# i = 0
# while i < len(nameList):
#     if "Lily" == nameList[i]:
#         nameList.remove(nameList[i])
#         continue
#     print(nameList[i])
#     i += 1
#
#
# print(nameList)
#
#
# name = input("请输入您的姓名:")
# if name in nameList:
#     print(f"您输入的姓名{name}不能使用")
# else:
#     print(f"您输入的姓名{name}可以使用")
#     nameList.append(name)
#
#
# print(nameList)
#
# nameList.insert(2,"Lily")
#
# print(nameList)
#
# nameList.reverse()
# print(nameList)
#
# newList = ["xiaoming","xiaohong","zhangsan"]
#
# nameList.extend(newList)
#
# print(nameList)
#
# nameList.reverse()
# print(nameList)
#
# if "Rose" in nameList:
#     index = nameList.index("Rose")
#     nameList[index] = "Rose2"
#
# print(nameList)


numList = [2,1,6,9,3,7]
numList.reverse()
print(numList)

numList.sort()
print(numList)

numList.sort(reverse=True)
print(numList)


nameList = ["Tom","Lily","Rose"]
myNameList = nameList.copy()
print(myNameList)

nameList1 = ["Tom1","Tom2","Tom3"]
nameList2 = ["Lily1","Lily2","Lily3"]
nameList3 = ["Rose1","Rose2","Rose3"]

nameLists = []
nameLists.append(nameList1)
nameLists.append(nameList2)
nameLists.append(nameList3)
print(nameLists)
print(nameLists[1][2])



newList = ["xiaoming","xiaohong","zhangsan","sdfa"]

nameList.extend(newList)

print(nameList)

for name in nameList:
    print(name,end=" ")