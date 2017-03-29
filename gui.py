# 文件搜索

# _*_ coding: utf-8 _*_
# GUI库有三个 Tkinter  WXPYTHON(版本想对于说比较老)  PYQT(用于开发大型项目)

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import os
import fnmatch

def search():
    text = entry_1.get()# 取值
    if not text:
        tkinter.messagebox.showinfo('提示', '请先输入关键字再搜索')
        return
        # tkinter.messagebox.askokcancel('提示', '这是一个消息框')
    fn = tkinter.filedialog.askdirectory() #选择文件夹 返回路径给fn
    fnlist = os.walk(fn) #列出目录
    for root, dirs, files in fnlist:
        listbox.delete(0, END)  # 插入之前删除所有数据
        for i in fnmatch.filter(files, entry_2.get()): # 过滤文件名
            filename = '%s/%s' %(root, i)
            listbox.insert(END, filename) # 往列表插入数据

# 文件双击事件
def click(event):
    index = listbox.curselection()[0] #选中的位置
    path = listbox.get(index)
    if not path:
        return
    window = Tk()
    window.title('查看文件')
    text = Text(window, width=100) # 多行文本框
    text.grid()
    fn_text = open(path).read()
    text.insert(END, fn_text)

# Tk().mainloop()  # Tk()是实例一个窗口对象。这里相当于用了2个函数
root = Tk()  # Tk()是实例一个窗口对象。这里相当于用了2个函数
root.title('PythonGUIDemo')
# 如果不写窗口大小，他会根据控件来自适应大小
root.geometry('+200+200') #更改窗口大小和位置  它有2个加号，第一个加号表示显示器左边到窗口左边的距离，第二个加号表示显示上边到窗口顶部的距离

# 传 父窗口 当只有一个窗口的时候，不传也可以，但是一旦窗口多了，他就不知道哪个是父窗口

# 添加一个 '关键词' lab
# grid是布局 网格是布局，可以看成excel表
# row 代表行   column 代表列   columnspan 可以跨越多个网格（相当于合并）
Label(root, text='关键字:').grid()

# 输入框
entry_1 = Entry(root)
entry_1.grid(row=0, column=1)

Label(root,text='文件类型:').grid(row=0, column=2)

entry_2 = Entry(root)
entry_2.grid(row=0, column=3)

# 按钮
button = Button(root, text='搜索', command=search)
button.grid(row=0, column=4)

# 表格
var1 = StringVar()
listbox = Listbox(root, width=80, listvariable=var1)
listbox.grid(row=1, column=0, columnspan=5)
listbox.bind('<Double-Button-1>', click)#绑定双击事件
root.mainloop()