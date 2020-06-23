

str1 = "0123456789"

print(str1[2:5:1])
print(str1[2:5:2])
print(str1[2:5])
print(str1[:6])
print(str1[2:])

print(str1[::-1])
print(str1[2::-1])
print(str1[:6:-1])

print(str1[-4:-1:-1])
print(str1[-1:-4:-1])


'''
    字符串的方法
    str.find(str, beg=0, end=len(string))
        方法检测字符串中是否包含子字符串 str ，
        如果指定 beg（开始） 和 end（结束） 范围，
        则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1
    str.rfind(str, beg=0 end=len(string))
         返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
        
    str.index(str, beg=0, end=len(string))
        方法检测字符串中是否包含子字符串 str ，
        如果指定 beg（开始） 和 end（结束） 范围，
        则检查是否包含在指定范围内，
        该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
    str.rindex(str, beg=0 end=len(string))
        返回子字符串 str 在字符串中最后出现的位置，
        如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间
        
    str.count(sub, start= 0,end=len(string))
        方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置.
        
    str.replace(old, new[, max])
        方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
        如果指定第三个参数max，则替换不超过 max 次。
    
    str.split(str="", num=string.count(str)).
        通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    
    str.join(sequence)
        方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        
        str.capitalize()
            将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
            注意：转换后，只有第一个字符大写，其他的字符全部改为小写
            
        str.title();
            方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
        str.istitle()
            方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
            
        str.lower()
            方法转换字符串中所有大写字符为小写。    
        str.islower()
            方法检测字符串是否由小写字母组成。
            
        str.upper()
            将字符串中的小写字母转为大写字母。            
        str.isupper()
            检测字符串中所有的字母是否都为大写。     
            
        str.strip([chars]); 去首尾字符
            用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
            注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        str.lstrip([chars]) 去首字符
            用于截掉字符串左边的空格或指定字符。
        str.rstrip([chars]) 去尾字符
            删除 string 字符串末尾的指定字符（默认为空格）.    
            
        str.ljust(width[, fillchar]) 左填充
            返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
            如果指定的长度小于原字符串的长度则返回原字符串。 
        str.rjust(width[, fillchar]) 右填充
             返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。
             如果指定的长度小于字符串的长度则返回原字符串。     
        str.center(width[, fillchar]) 居中
            返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。 
            
        str.startswith(str, beg=0,end=len(string));
            用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
            如果参数 beg 和 end 指定值，则在指定范围内检查。  
        str.endswith(suffix[, start[, end]])
            用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
            可选参数"start"与"end"为检索字符串的开始与结束位置。  
            
        str.isalpha()  判断是否为全字母
            检测字符串是否只由字母组成    
        str.isdigit()  判断是否全是数字
            检测字符串是否只由数字组成。   
        str.isalnum()  判断是否只有字母和数字组成的字符串
            检测字符串是否由字母和数字组成。
        str.isspace()  判断是否只有空格
            检测字符串是否只由空格组成。    
        

'''


str2 = "hello world and itcast and itheima and Python"
new0 = str2.replace("and","he")
new1 = str2.replace("and","he",1)
print(str2)
print(new0)
print(new1)


list1 = str2.split("and")
list2 = str2.split("and",2)
print(list1)
print(list2)


joinStr = "-".join(["aaa","bbb","ccc"])
print(joinStr)

str = "hello world and itcast and itheima and Python"

str1 = str.capitalize()
print(str1)

str2 = str.title()
print(str2)
print(str2.istitle())

str3 = str.upper()
print(str3)
print(str3.isupper())

str4 = str.lower()
print(str4)
print(str4.islower())


str = "    删除 string 字符串末尾的指定字符（默认为空格）    "

print(str)
str1 = str.lstrip()
str2 = str.rstrip()
str3 = str.strip()
print(str1)
print(str2)
print(str3)

str = "0000删除 string 字符串末尾的指定字符（默认为空格）00000"

print(str)
str1 = str.lstrip('0')
str2 = str.rstrip('0')
str3 = str.strip('0')
print(str1)
print(str2)

print(str3)



str = "hello world and itcast and itheima and Python"
print(str.startswith("hello"))
print(str.startswith("and", 12, len(str)))

print(str.endswith("and",0,-7))



str1 = "hello13441"
str2 = "hello"
str3 = "6547654"
print(str1.isdigit())
print(str1.isalpha())
print(str1.isalnum())
print(str2.isalpha())
print(str3.isdigit())

str = "     "
str2 = "1 2 3 "
print(str.isspace())
print(str2.isspace())

