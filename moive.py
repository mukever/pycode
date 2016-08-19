#encoding=utf-8
__author__ = 'mukever'

from bs4 import BeautifulSoup;
import re;
import requests;
import urllib2;
import urllib;
def getHtml(url):
    page = urllib2.urlopen(url).read();
    res = re.compile(r'<META http-equiv=Content-Type content="text/html; charset=(.*)">');
    co = re.search(res,page);
    print co.group(1);
    page.decode('utf8').encode('gb2312');
    return page;

html = getHtml("http://www.dytt8.net/");
print html;