# 闭包
# 意义： 安全性
# 输出1 2 3 4 5 6
# 每一次都会加一再输出
def take_num():
    x=0
    def cuonte():
        nonlocal x
        x+=1
        return x
    return cuonte
cuonter=take_num()
print(cuonter())
print(cuonter())
print(cuonter())
print(cuonter())
print(cuonter())
print(cuonter())