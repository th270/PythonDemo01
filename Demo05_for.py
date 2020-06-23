

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1

print("sum ==",sum)

n = 1
m = 1

while m <= 9:
    n = 1
    while n <= 9:
        if n <= m:
            print(n,"*",m, "=",m*n ,end=" | ")
        n += 1
    print()
    m += 1



#for in  循环
for  i  in "abcdefg":
    print(i,end=" ")

print()

for n in [10,20,30,40]:
    print(n , end=" ")