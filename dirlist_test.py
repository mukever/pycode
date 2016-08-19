# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding('utf8')
webxml= ET.parse("config.xml")
web_names=webxml.findall('web_name')
#print web_names
for web_name in web_names:
  print web_name.attrib['name']
  web_lis = web
    all_attrs = web_li.getchildren()
    #print all_attrs
    for all_attr in  all_attrs:
      #print all_attr
      if(all_attr.attrib['name']=="start_pattrern"):
        print "网址前缀："+all_attr.text
      if(all_attr.attrib['name']=="end_pattrern"):
        print "网址后缀："+all_attr.text
      if(all_attr.attrib['name']=="page_num"):
        print "构造页数："+all_attr.text
      if(all_attr.attrib['name']=="special"):
        if(all_attr.attrib['id']=="0"):
          print "无需特殊处理"
        else:
          print  "需要特殊处理——处理符号为："+all_attr.text
      if(all_attr.attrib['name']=="li_attr"):
        li_attrs = all_attr.getchildren()
        for li_attr in li_attrs:
          print "需要抓取列表url的属性为"+li_attr.attrib['name']+ "=" +li_attr.text
      if(all_attr.attrib['name']=="filename"):
        print  "需要保存的文件名："+all_attr.attrib['save']
        article_attrs = all_attr.getchildren()
        for article_attr in article_attrs:
          print  article_attr.attrib['name']+ ":" + article_attr.getchildren()[0].attrib['name']+"="+article_attr.getchildren()[0].text


