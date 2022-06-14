# map(函数名, 可迭代对象)
# 作用：映射
# 可迭代对象中的每个元素传给函数
# 将对应的返回值放到map对象中返回
# 返回值：map对象(不能直接输出,可以用list()转为列表再输出)

# 将列表内的元素平方并放回列表
map_res = map(lambda x: pow(x,2), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(map_res)
print(type(map_res))
print(list(map_res))

# 求两个列表（一个内是奇数，另一个内则是偶数）第一个列表的第一个元素加，第二个列表中的第一个元素
map_res = map(lambda x, y, z: x+y+z, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(map_res))

# 求两个列表（一个内是奇数，另一个内则是偶数）第一个列表的第一个元素加，第二个列表中的第一个元素
map_res = map(lambda name_str: name_str[0].upper()+name_str[1::].lower(), ['luCA', 'lei', 'StEvEvEvEvN', 'pTTER', 'hhh'])
print(list(map_res))
