import re
# print(re.match(r'(\w{3}).*(\1)', "abceeeabc456abc789").group())
str_abc = re.match(r'(\w{3}).*(\1)', "abceeeabc456abc789").group()
print(str_abc)
list = re.findall(r'(\w{3})', str_abc)
print(list)
for i in list:
    if i == 'abc':
        list.remove(i)
print(list)
# print(re.match(r'(\w{3}).*?', "abceeeabc456abc789").group())
# print(re.match(r'(\w{3}).*', "abceeeabc456abc789").group())
# print(re.match(r'(\w{3}).*', "abceeeabc456abc7891\n123").group())

# print(re.match(r'(\w{3})(.|\n)*', r"abceeeabc456abc7891\n123").group())
# print(re.match(r'(\w{3})(.|\n)*', r"abceeeabc456abc7891\n123").groups())
# print(re.match(r'(\w{3})', r"abceeeabc456abc7891\n123").groups())

# print(re.match(r'(\w{3}){1}', r"abceeeabc456abc7891\n123").groups())
# print(re.match(r'(\w{3}){2}', r"abceeeabc456abc7891\n123").groups())
# print(re.match(r'(\w{3}){3}', r"abceeeabc456abc7891\n123").groups())

# print(re.match(r'(\w{3}){1}', r"abceeeabc456abc7891\n123").group())
# print(re.match(r'(\w{3}){2}', r"abceeeabc456abc7891\n123").group())
# print(re.match(r'(\w{3}){3}', r"abceeeabc456abc7891\n123").group())
# print(re.match(r'(\w{3})(.|\n)*', r"abceeeabc456abc7891\n123").group(1))
# print(re.match(r'(\w{3})(.|\n)*', r"abceeeabc456abc7891\n123").group(2))

# print(re.match(r'(\w{3})(.|\n)*', "abceeeabc456abc7891\n123").group(3))