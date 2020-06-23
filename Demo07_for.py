


i = 0
result = 0
while i <= 100 :
    if i%2 == 0:
        result += i
    i += 1

print(result)


j = 0
result = 0
while j <= 100:
    result += j
    j += 2

print(result)

i = 1
while i <=5 :
    print("我错了！")
    if i == 4 :
        break
    i += 1
else:
    print("OK")