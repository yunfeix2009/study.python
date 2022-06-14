# filter(函数名, 可迭代对象)
# 作用：过滤可迭代对象
# 将可迭代对象中的每个元素传给函数进行判断
# 将返回值为True的元素放到filter对象中返回
# 返回值：filter对象(不能直接输出,可以用list()转为列表再输出)

def is_odd(n):
    if n%2 ==1 :
        return True
    return False
tempfilter=filter(is_odd,range(0,11))
print(tempfilter)
print(list(tempfilter))


# 计算平方，filter与常规的实例
# math库的sqrt()函数开平方
# 常规
import math
sq=[]
for i in range(1,101):
    sqrt=math.sqrt(i)
    if sqrt%1==0:
        sq.append(i)
    else:
        pass
print(sq)
# filter
import math
def is_int(n):
    if math.sqrt(n)%1==0:
        return True
    return False
temp=filter(is_int,range(1,101))
print(list(temp))


# 统计sentences中"learning"出现的次数
sentences = ['The', 'Deep', 'Learning', 'textbook', 'is', 'a', 'resource', 'intended', 'to', 'help', 'students', 'and',
             'practitioners', 'enter', 'the', 'fild', 'of', 'machine', 'learning', 'in', 'general', 'and', 'deep',
             'learning', 'inparticular', '.']
def flag(str):
    if str == 'learning':
        return True
    return False
tempfilter = filter(flag, sentences)
print(len(list(tempfilter)))