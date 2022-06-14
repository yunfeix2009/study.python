
import re
y = "Today is nice. My email is 123@qq.com. Tom’s email is aaa@163.com, he will come later. My teacher’s email is bbb@126.com, and he also use 33333@163.com."
temp = re.compile('.{3,5}.?@.{3,4}com')
print(re.findall(temp,y))