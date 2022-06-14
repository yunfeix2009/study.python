import re

a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)
res = re.findall(r"\d+|[a-zA-Z]+", a)

# for i in res:
#     if i in list:
#         list.remove(i)
# new_str = " ".join(list)
# print(new_str)

# print(res)
# dif_elements = [y for y in list if y not in res]
# print(dif_elements)

# print(res)
# set_list = set(list)
# set_res = set(res)
# finally_set = set_list - set_res
# print(finally_set)

# print(res)
# same_elements = [x for x in list if x in res]
# dif_elements = [y for y in (list+res) if y not in same_elements]
# print(same_elements)
# print(dif_elements)