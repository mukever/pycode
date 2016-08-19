 # -*- coding: UTF-8 -*-

#windows 环境下安装 lxml python
#1、首先保证你的python 环境安装完善
#2、把http://peak.telecommunity.com/dist/ez_setup.py 文件下载到电脑上
#3、打开运行 cmd  执行：python ez_setup.py
#4、安装完毕 ,PATH环境变量里面添加路径：如：E:\python27\Scripts（E:\python27 是python的安装路径）
#5、cmd执行:easy_install virtualenv
#6、下载 lxml文件：http://pypi.python.org/pypi/lxml/2.3/
#7、cmd 执行 easy_install （文件路径）\lxml-2.3.py2.7.win32.egg


import io
import re
import urllib
import urllib2
import bs4
import lxml
import sys
import  xml.dom.minidom

reload(sys)
sys.setdefaultencoding('utf8')
header = {
    "Accept-Language":"zh-CN,zh;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
}

tip ={"光明网":{"时政国内":["http://politics.gmw.cn/node_9840",".htm"],
                 "国际要闻":["http://world.gmw.cn/node_4661",".htm"]
             }} #字典-网站名及其下属列表


# 创建手动创建url列表
def Create_Url(tip,k,name,li):
    Url_List = []
    for i in range(1,k):
        s = "_"
        if i==1:
            s=""
            i=""
        li_st = tip.get(name).get(li)
        Url_List.append(li_st[0]+s+i.__str__()+li_st[1])   # 构建列表的url
        print li_st[0]+s+i.__str__()+li_st[1]
    return Url_List


#打开网页，返回html
def getHtml(url,header):
    req = urllib2.Request(url,None,header)
    response = urllib2.urlopen(req,None,60)
    the_page = response.read()
    return  the_page


#获取内容
def Get_Content(url,header):
    page = getHtml(url,header)
    #print page
    con = bs4.BeautifulSoup(page)
    con_title = con.find( id="articleTitle").text
    con_time = con.find( id="pubTime").text
    con_context = con.find( id="contentMain").text
    #text = open("result.txt","w")
    return con_title +"\t"+con_time+"\n"+"文章内容："+con_context
    #text.write("文章标题："+con_title +"\n"+"发布时间"+con_time+"\n"+"文章内容：\n"+con_context)
    #text.close()
#获取列表url多应详情的url
def Get_List_Url(li,tag_name,tag_attr,header):
    m=0;
    text = open("result.txt","w")
    for i in  li:
        b = bs4.BeautifulSoup(getHtml(i,header));
        print tag_name
        res1 = b.find_all(class_=tag_attr[0])
        res2 = b.find_all(class_ =tag_attr[1])
        fir_http = i.split('/')[2]
        #print fir_http
        #print res
        for k in  res1:
            RES_HTTP="http://"+fir_http+"/"+ k.a["href"]
            print RES_HTTP
            text.write(Get_Content(RES_HTTP,header))
            m+=1
        for k in  res2:
            RES_HTTP="http://"+fir_http+"/"+ k.a["href"]
            print RES_HTTP
            text.write(Get_Content(RES_HTTP,header))
            m+=1
    print m
    text.close()


if __name__ == '__main__':
    keys = tip.keys()
    for key in keys:
        li_keys = tip.get(key).keys()
        for li_key in li_keys:
            t = Create_Url(tip,10,key,li_key)
            Get_List_Url(t,'class_',["channel-newsGroup","channel-newsGroup"],header)