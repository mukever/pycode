# -*- coding: UTF-8 -*-
#author : mukever
#time :2015/12/30
#option :everything

import io
import re
import urllib
import urllib2
import bs4
import lxml
import sys
import string
import dir_list
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    "Accept-Language":"zh-CN,zh;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
}


# 创建手动创建url列表
#tip 即为构建的字典
def get_Create_Url(tip):
    #获取相关配置信息
    start = tip.get('start')
    end = tip.get('end')
    num_of_page = tip.get('pagenum')
    special_char = tip.get('special_char')
    special = tip.get('special')

    #构建url
    Url_List = []
    for  i in  range(1,string.atoi(num_of_page,10)):
        if i==1 and string.atoi(special,10):
            li_urls = start+i.__str__()+end
        elif i==1 and  not string.atoi(special,10):
            li_urls = start+end
        else:
            li_urls = start+special_char+i.__str__()+end
        Url_List.append(li_urls)
    #返回列表
    return  Url_List


#获取网页源代码
def get_Html(url,headers):
    req = urllib2.Request(url,None,headers)
    response = urllib2.urlopen(req,None,60)
    the_page = response.read()
    return  the_page

#得到网页列表链接的url
def get_liurl_of_webli(url_list,attr_dir,headers):

    link = []
    #依次打开各页的url 并得到页面内需要的的url链接
    for url in  url_list:

        #得到源码
        html = get_Html(url,headers)

        #生成bs对像
        bs = bs4.BeautifulSoup(html)

        #得到需要抓取的属性
        li_attrs_name = attr_dir.keys()

        #在列表中是不需要是否补全的这个属性的
        li_attrs_name.remove("completion")

        #遍历属性值，寻找所有节点
        for li_attr in li_attrs_name:
            link_urls = bs.find_all(li_attr=attr_dir.get(li_attr))
            #提出每一个节点的url  并判断是否需要补全 0代表不需要补全
            for link_url in link_urls:
                if attr_dir.get('completion')=="1":
                    fir_http = url.split('/')[2]
                    RES_HTTP="http://"+fir_http+"/"+ link_url.a["href"]
                    link.append(RES_HTTP)
                    print RES_HTTP
                else:
                    RES_HTTP = link_url.a["href"]
                    link.append(RES_HTTP)

    return link

#获取内容
def get_Content(url, headers, art_dir,art_title_key,art_time_key,art_context_key):

    page = get_Html(url,headers)
    #print page
    cont = bs4.BeautifulSoup(page)

    #每一个都是字典
    art_title = art_dir.get('art_title')
    art_time = art_dir.get('art_time')
    art_context = art_dir.get('art_context')

    #得到结果
    if art_title_key=="class":
        title = cont.find(class_=art_title.get(art_title_key))
    else:
        title = cont.find(art_title_key= art_title.get(art_title_key))

    if art_time_key=="class":
        time = cont.find(class_=art_title.get(art_time_key))
    else:
        time = cont.find(art_time_key= art_title.get(art_time_key))

    if art_context_key=="class":
        content = cont.find(class_=art_title.get(art_context_key))
    else:
        content = cont.find(art_context_key= art_title.get(art_context_key))
    text = open("result.txt","a")
    #return con_title +"\t"+con_time+"\n"+"文章内容："+con_context
    text.write("文章标题："+title +"\n"+"发布时间"+time+"\n"+"文章内容：\n"+content)
    text.close()


if __name__ == '__main__':

    path = "config.xml"
    #得到xml字典
    result_dir = dir_list.get_dir_list(path)
    #得到网站的名称
    web_names = result_dir.keys()
    print web_names[0]

    #依次遍历
    for web_name in  web_names:
        #得到需要抓取数据的网站列表
        web_lis = result_dir.get(web_name)
        print web_lis

        #依次遍历
        for web_li in web_lis:
            #得到各个属性字典
            print web_li
            attrs = web_li.keys()
            #构建网页
            Url_List = get_Create_Url(attrs)
            #得到每一页列表的链接
            links = get_liurl_of_webli(Url_List,attrs,headers)
            #遍历得到详情

            art_title = attrs.get('art_title')
            art_time = attrs.get('art_time')
            art_context = attrs.get('art_context')

            #得到属性关键字
            art_title_key = art_title.keys[0]
            art_time_key = art_time.keys[0]
            art_context_key = art_context.keys[0]

            for link in links:

                get_Content(link,headers,attrs,art_title_key,art_time_key,art_context_key)
