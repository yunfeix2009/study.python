# 导入
import tkinter as tk,re
from tkinter import Button

# 可视化窗口
window = tk.Tk()
window.title('qq邮箱提取')
window.geometry('800x1000')

# 定义一个临时字符串

str=''

# 提取函数
def got_qq():
    global str
    t=re.compile('(\d{5,25}) ')
    qqnum=re.findall(t, context)
    print(qqnum)
    for item in qqnum:
        str=str+item+'@qq.com'+'\n'
    qqnumprint.insert(tk.END,str)

# 保存函数
def save_qq():
    with open('qqmail.txt', 'w') as output:
        output.write(str)

# 控件定义
got: Button = tk.Button(text="提取",command = got_qq) # 添加提取按钮
got.pack()
save: Button = tk.Button(text="保存", command=save_qq)
save.pack()
qqtxt=tk.Text(window, height=10)
qqtxt.pack()
qqnumprint = tk.Text(window,height=20,width=20)
qqnumprint.pack()

# 添加源文件
with open('QQstring.txt', 'r', encoding='utf-8') as file:
    context = file.read()
qqtxt.insert(tk.END,context)

# 显示界面
window.mainloop()