
list1 = [1,2,3,4,5]
t1 = (10,20,30,40,50)
s1 = {100,200,300,400,500}

#list()
print(list(t1))
print(list(s1))

#tuple()
print(tuple(list1))
print(tuple(s1))

#set()
print(set(list1))
print(set(t1))


for i in t1:
    print(i,end=" ")


