# 递归函数
# 定义：函数自己调用自己
# 意义：
# 1使代码更整洁、优雅
# 2将复杂任务分解成简单的子问题

# 用递归实现阶乘


# 用循环来完成
def recursion(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1
    return result
res = recursion(4)
print(res)


# 用递归
def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n - 1)
res = recursion(3)
print(res)


# 求n的m次方 power函数
def power(n, m):
    if m == 1:
        return n
    return n * power(n, m - 1)
print(power(2, 10))