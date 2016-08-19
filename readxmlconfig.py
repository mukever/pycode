 # -*- coding: UTF-8 -*-


import bs4

def formatXML(path):
    ret = {}
    bs = bs4.BeautifulSoup(open(path))
    web_names =  bs.web_name
    print web_names
    for web_name in web_names.next_siblings:
        print web_name

result = formatXML("config.xml")
print result