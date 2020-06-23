
ADD_INFO = 1
DEL_INFO = 2
MODIFY_INFO = 3
QUERY_INFO = 4
SHOW_INFO = 5
EXIT_SYSTEM = 6

from StudentSystem.src.SystemService import infoPrint
from StudentSystem.src.SystemService import inputYourIndex
from StudentSystem.src.SystemService import addStudent
from StudentSystem.src.SystemService import showStudentInfos
from StudentSystem.src.SystemService import delStudent
from StudentSystem.src.SystemService import queryStudent
from StudentSystem.src.SystemService import modifyStudent

while True:
    index = inputYourIndex()
    if ADD_INFO == index:
        # print("添加")
        addStudent()
    elif DEL_INFO == index:
        # print("删除")
        delStudent()
    elif MODIFY_INFO == index:
        # print("修改")
        modifyStudent()
    elif QUERY_INFO == index:
        # print("查询")
        queryStudent()
    elif SHOW_INFO == index:
        # print("显示")
        showStudentInfos()
    elif EXIT_SYSTEM == index:
        print("退出系统！欢迎再次使用")
        break

