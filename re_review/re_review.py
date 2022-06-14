# import re
# # re_email = r'\w+@(163|162|Gmail|yahoo).com'
# re_email = r'^[a-zA-Z0-9_]{0,19}@(163|162|Gmail|yahoo)\.com'
# # re_email = r'^[0-9a-zA-Z_]{0,19}@(163|162)\.com'
#
# # re_email = '^steven@163.com'
# # re_email = '^[a-zA-Z0-9_]{5,20}@163.com'
# email_address = input('请输入邮箱')
# # res = re.search(re_email, email_address)
# res=re.match(re_email,email_address)
# print(res)
# print(email_address)
# print(type(res))

import re
re_email = r'^[a-zA-Z0-9_]{6,20}@(163|162|Gmail|yahoo)\.com'
email_address = input('请输入邮箱')
res = re.search(re_email, email_address)
print(res)
print(email_address)
print(type(res))
print(res.group())