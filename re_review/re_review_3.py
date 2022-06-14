import re
# re_phone_number = r'(86|1|11)-\d{4}-\d{3}'
re_phone_number = r'1[358]\d{9}'
phone_number = input('请输入手机号')
res = re.search(re_phone_number, phone_number)
print(res)
print(phone_number)
print(type(res))
# print(res.group())

