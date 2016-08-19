# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_dir_list(path):

    #res 为保存xml结果的字典，首先将其置为空
    res = {}

    #构建ETree
    webxml= ET.parse(path)

    #找到所有的网站名称
    web_names=webxml.findall('web_name')

    #测试打印每个网站的信息
    #print web_names

    #去找每一个网站的所有信息
    for web_name in web_names:

      #打印每一个网站的名称
      #print web_name.attrib['name']
      #得到网站的名称，并将其设为key，    value设为空（后面信息收集完毕后再添加value）
      key = web_name.attrib['name']
      res[key]=''

      #value 也是一个字典，初值为空
      key_value = {}

      #找到该网站的各个列表分类，web_lis为一个列表
      web_lis = web_name.getchildren()

      #循环一下
      for web_li in web_lis:

        #找到每一个分类的名称
        #print web_li.attrib['name']
        web_li_name =  web_li.attrib['name']

        #同样将其加入主字典value的键中
        key_value[web_li_name]=''

        #找到在网页中爬去该分类需要的url及其节点的属性  和  爬取详情的url及其节点的属性
        all_attrs = web_li.getchildren()
        #打印测试一下
        #print all_attrs
        value_dir={}
        #找到xml文件中的该网站在这个分类上的各个重要信息
        for all_attr in  all_attrs:
          #print all_attr

          #网页前缀
          if(all_attr.attrib['name']=="start_pattrern"):
            #打印测试
            #print "网址前缀："+all_attr.text
            #将其计入字典中
            value_dir['start_pattrern']=all_attr.text

          #网页后缀
          if(all_attr.attrib['name']=="end_pattrern"):
            #print "网址后缀："+all_attr.text
            value_dir['end_pattrern']=all_attr.text

          #需要爬取得网页数
          if(all_attr.attrib['name']=="page_num"):
            #print "构造页数："+all_attr.text
            value_dir['page_num']=all_attr.text

          #第一页是否需要特殊处理
          if(all_attr.attrib['name']=="special"):
            if(all_attr.attrib['id']=="0"):
              #print "无需特殊处理"
              key_value['special']='0'
              key_value['special_char']=""
            else:
              #print  "需要特殊处理——处理符号为："+all_attr.text
              key_value['special']='1'
              key_value['special_char']=all_attr.text


          #当节点为列表的属性时，其属性为一个字典
          li_attr_dir = {}
          if(all_attr.attrib['name']=="li_attr"):
            li_attrs = all_attr.getchildren()
            for li_attr in li_attrs:
              #print "需要抓取列表url的属性为"+li_attr.attrib['name']+ "=" +li_attr.text
              li_attr_dir[li_attr.attrib['name']]=li_attr.text


          #将一个字典赋给li_attr 这个住键
          key_value['li_attr']=li_attr_dir


          if(all_attr.attrib['name']=="filename"):
            # 测试
            #print  "需要保存的文件名："+all_attr.attrib['save']
            key_value['save_file_name']=all_attr.attrib['save']

            article_attrs = all_attr.getchildren()
            for article_attr in article_attrs:
              article_dir={}
              #print  article_attr.attrib['name']+ ":" + article_attr.getchildren()[0].attrib['name']+"="+article_attr.getchildren()[0].text
              article_dir[ article_attr.getchildren()[0].attrib['name']]=article_attr.getchildren()[0].text
              key_value[article_attr.attrib['name']]=article_dir

      key_value[web_li_name]=value_dir
    res[key]=key_value
    return  res

