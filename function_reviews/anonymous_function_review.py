# 匿名函数 (lambda表达式)
# 语法：lambda 参数:表达式
# 作用：相当于一个没有名称的函数


# +1的函数
# 常规
def add1(arg):
    return arg + 1
print(add1(2))
# lambda 表达式
add_1 = lambda arg: arg + 1
print(add1(2))

# 求和
sum = lambda num1, num2: num1 + num2
print(sum(1, 2))

# 求三个数的平均值
average = lambda x, y, z: (x + y + z) / 3
print(average(1, 2, 3))


# lambda 参数:表达式
# lambda & reduce
import functools
res = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(res)
# 列表求和