
#1- 递归的条件：
#   1-1 函数自己调用自己
#   1-2 函数必须有出口
#2- 递归有最深递归次数：
#   2-1 Previous line repeated 995 more times
#       maximum recursion depth exceeded in comparison

def sum_numbers(num):
    if 1 == num:
        return 1
    return num + sum_numbers(num -1)

# print(sum_numbers(1000))#Previous line repeated 995 more times   maximum recursion depth exceeded in comparison
print(sum_numbers(100))

