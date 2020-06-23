
QUERY_DEL_BY_ID = 1
QUERY_DEL_BY_NAME = 2
QUERY_DEL_EXIT = 3

MODIFY_NAME = 1
MODIFY_AGE = 2
MODIFY_EXIT = 3

studentInfos = []

student=["id","name","age"]

def printStarts(count = 20):
    return "*"*count

def infoPrint():
    print(printStarts(100))
    print(f"\t\t\t\t\t{printStarts()}1-添加学员{printStarts()}")
    print(f"\t\t\t\t\t{printStarts()}2-删除学员{printStarts()}")
    print(f"\t\t\t\t\t{printStarts()}3-修改学员{printStarts()}")
    print(f"\t\t\t\t\t{printStarts()}4-查询学员{printStarts()}")
    print(f"\t\t\t\t\t{printStarts()}5-显示所有学员{printStarts(16)}")
    print(f"\t\t\t\t\t{printStarts()}6-退出系统{printStarts()}")
    print(printStarts(100))


def printStudentInfos(allInfos):
    for studentInfo in allInfos:
        for i in student:
            print(f"{i} = {studentInfo[i]}",end="\t")
        print()


def isExistID(newId):
    for studentInfo in studentInfos:
        if newId == studentInfo["id"]:
            return True
    return False


def inputStudentID(msg):
    id = None
    while True:
        id = input(f"{msg}：")
        if id.strip() != "":
            break
    return id

def inputStudentName(msg):
    name = None
    while True:
        name = input(f"{msg}：")
        if name.strip() != "":
            return name

def inputStudentAge(msg):
    age = None
    while True:
        age = input(f"{msg}：")
        if not age.isdigit():
            continue
        break;
    return age

def inputYourIndex():
    while True:
        infoPrint()
        num = input("请输入您的选择序号：")
        if not num.isdigit():
            continue
        else :
            break
    return int(num)

def inputNewStudentInfo():
    studentDict = {}
    newStudentInfo = []

    while True:
        newId = inputStudentID("请输入新增学生的ID")
        if not isExistID(newId):
            break

    newStudentInfo.append(newId)

    newName = inputStudentName("请输入新增学生的姓名")
    newStudentInfo.append(newName)

    newAge = inputStudentAge("请输入新增学生的年龄")
    newStudentInfo.append(newAge)

    studentDict = {student[i]:newStudentInfo[i] for i in range(len(student))}
    return studentDict

def addStudent():
    #1- 输入学生信息
    newStudentDict = inputNewStudentInfo()
    #2- 存入信息
    studentInfos.append(newStudentDict)
    print("添加成功！")
    showStudentInfos()


def delStudentByIdOrName(delId,delName):
    if delId is not None:
        #根据ID删除
        for i,studentInfo in enumerate(studentInfos,0):
            if delId == studentInfo["id"]:
                studentInfos.pop(i)
                print("删除成功！")
                return


    elif delName is not None:
        #根据姓名删除
        for i,studentInfo in enumerate(studentInfos,0):
            if delName == studentInfo["name"]:
                studentInfos.pop(i)
                print("删除成功！")
                return
    print("没有您要删除的信息！")


def delStudent():
    delId = None
    delName = None
    while True:
        print(printStarts(100))
        print(f"\t\t\t\t\t{printStarts()}1-根据ID删除 {printStarts()}")
        print(f"\t\t\t\t\t{printStarts()}2-根据姓名删除 {printStarts(18)}")
        print(f"\t\t\t\t\t{printStarts()}3-退出删除 {printStarts(22)}")
        print(printStarts(100))
        num = inputYourIndex()
        if QUERY_DEL_BY_ID == num:
            delId = inputStudentID("请输入删除学生的ID")
        elif QUERY_DEL_BY_NAME == num:
            delName = inputStudentName("请输入删除学生的姓名")
        elif QUERY_DEL_EXIT == num:
            return
        else:
            continue
        delStudentByIdOrName(delId,delName)
        print()
        break;

def queryStudentByIdOrName(queryId,queryName):
    queryStudents = []
    for studentInfo in studentInfos:
        if queryId == studentInfo["id"] or queryName == studentInfo["name"]:
            queryStudents.append(studentInfo)
    return queryStudents

def queryStudentInfo():
    queryStudents = []
    queryId = None
    queryName = None
    while True:
        print(printStarts(100))
        print(f"\t\t\t\t\t{printStarts()}1-根据ID查询 {printStarts()}")
        print(f"\t\t\t\t\t{printStarts()}2-根据姓名查询 {printStarts(18)}")
        print(f"\t\t\t\t\t{printStarts()}3-退出查询 {printStarts(18)}")
        print(printStarts(100))
        num = inputYourIndex()
        if QUERY_DEL_BY_ID == num:
            queryId = inputStudentID("请输入查询学生的ID")
        elif QUERY_DEL_BY_NAME == num:
            queryName = inputStudentName("请输入查询学生的姓名")
        elif QUERY_DEL_EXIT == num:
            return
        else:
            continue
        break;
    queryStudents = queryStudentByIdOrName(queryId,queryName)

    return queryStudents

def queryStudent():
    queryStudents = queryStudentInfo()
    if  queryStudents:
        print("您要查询的学生信息如下：")
        printStudentInfos(queryStudents)
    else:
        print("没有查询到相关信息！")


def modifyStudentName(ids):
    global studentInfos
    for student in studentInfos:
        if student.get("id") in ids:
            modifyName = inputStudentName(f"您想把{student.get('name')}修改为")
            student["name"] = modifyName

def modifyStudentAge(ids):
    global studentInfos
    for student in studentInfos:
        if student.get("id") in ids:
            modifyAge= inputStudentAge(f"您想把{student.get('age')}修改为")
            student["age"] = modifyAge

def modifyStudentInfo (ids):
    modifyName = None
    modifyAge = None
    while True:
        print(printStarts(100))
        print(f"\t\t\t\t\t{printStarts()}您想修改什么信息？ {printStarts()}")
        print(f"\t\t\t\t\t{printStarts()}1-修改姓名 {printStarts()}")
        print(f"\t\t\t\t\t{printStarts()}2-修改年龄 {printStarts(18)}")
        print(f"\t\t\t\t\t{printStarts()}3-退出查询 {printStarts(18)}")
        print(printStarts(100))
        num = inputYourIndex()
        if MODIFY_NAME == num:
            # modifyName = inputStudentName("请输入需要修改学生的姓名")
            modifyStudentName(ids)
        elif MODIFY_AGE == num:
            # modifyAge = inputStudentAge("请输入需要修改学生的年龄")
            modifyStudentAge(ids)
        elif MODIFY_EXIT == num:
            return
        else:
            continue
        break;
    # modify(ids,modifyName,modifyAge)
    print("修改完成！")
    showStudentInfos()

def getModifyIds():
    ids = []
    print("请先查询到您想修改学生的信息")
    modifyStudents = queryStudentInfo()
    for student in modifyStudents:
        id = student.get("id")
        ids.append(id)
    return ids

def modifyStudent():
    ids = getModifyIds()
    modifyStudentInfo(ids)

def showStudentInfos():
    printStudentInfos(studentInfos)
