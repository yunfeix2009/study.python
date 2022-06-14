# reduce(函数名, 可迭代对象)
# 作用：累积
# 对可迭代对象中元素进行累积
# 返回值：返回函数累积计算的结果



# 先对列表中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用add函数运算
from functools import reduce
def add(x, y):
    return x + y
res = reduce(add, [1, 2, 3, 4, 5])
# 计算列表和
print(res)

# 求所有元组的第一个元素之和，和，第二个元素之和
def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
temp = reduce(add, [(1, 4), (2, 3), (5,6)])
print(temp)

# 求元组所有元素之和
# 坐标为零之和，坐标为一，得到一个元组
def add_tuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
temp = reduce(add, [(1, 4), (2, 3), (5,6)])
# 求上一步得到的元组之和
def add_list(x, y):
    return x + y
res = reduce(add_list, temp)
print(res)

# 计算从一到一百的平方和
def add(x, y):
    return x + y
reduce_res = reduce(add, [pow(i,2) for i in range(1,101)])
print(reduce_res)