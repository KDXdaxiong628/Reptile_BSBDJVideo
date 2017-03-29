# 爬虫爬取百思不得姐视频中第一页视频

# _*_ coding:utf-8 _*_


from tkinter import *
from tkinter.scrolledtext import ScrolledText # 引入滚动条
import urllib, requests
import urllib.request
import re # 正则表达式
import threading # 多线程处理与控制
import time

url_name = [] # 空列表 装地址和名称这些
# 1 如何解决网站禁止爬虫-----加上我们的头部信息 User-Agent（浏览器信息），伪装成浏览器进行访问
# 读取网页源码  import urllib   a = urllib.urlopen('网址')     a.read()    如果想读取第一行就是 a.readline()
a = 1 #页数
def get():
    global a  #改变全局变量，因为a会发生改变
    hd = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0'}
    url = 'http://www.budejie.com/video/' + str(a)
    var1.set('已经获取第%s页视频' % a)
    # 对网站发送get请求   .text是获取源码
    html = requests.get(url, headers = hd).text
    # print(html)
    # 正则表达式  re.S是匹配换行符的意思
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S)
    url_contents = re.findall(url_content, html)
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)">' # 匹配mp4格式的文件
        url_items = re.findall(url_reg, i)
        if url_items:# 如果有视频存在，我才匹配名字，如果没有视频，我就直接跳过   .*?   是代表匹配未知字符的意思 ，加一个()是代表不仅要匹配的，我还要取出来
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>', re.S)
            name_items =re.findall(name_reg, i)
            for i, k in zip(name_items, url_items):
                # 往列表中追加元素
                url_name.append([i, k])
                print(i, k)
    return url_name

id = 1 #代表视频个数
def write():
    global id
    while id<10:
        url_name = get()#调用获取视频和名字
        for i in url_name:
            #下载
            urllib.request.urlretrieve(i[1], '/Users/liaohang/Desktop/Python学习/pachongVideo/%s.mp4' % (i[0]))
            text.insert(END, str(str(id) + '.' + i[1] + '\n' + i[0] + '\n'))
            url_name.pop(0)
            id+=1
    var1.set('大雄:视频链接抓取完毕,voer!')

# 多线程
def start():
    th = threading.Thread(target = write)
    th.start()# 启动线程


root = Tk()
root.title('爬虫')
root.geometry('+200+200')

# 创建滚动条
text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()

# 按钮
button = Button(root, text = '开始爬取', font=('微软雅黑', 10), command = start)
button.grid()

# Lable  fg 代表颜色
var1 = StringVar() #通过tk方法绑定一个变量
lable = Label(root, font=('微软雅黑', 10), fg = 'red', textvariable = var1)
lable.grid()
var1.set('大雄时刻准备着...')

root.mainloop() # 创建窗口指令

