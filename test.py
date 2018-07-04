import requests
import re
from bs4 import BeautifulSoup

def demo_regex():
    str='abfg1234dget256fd3'
    str2='wujiang@gmail.com,1xiaoshuigong@qq.com,nihao@163.com,n@163.com'
    str3='<html><head>title</head><body>content</body></html>'
    pa=re.compile('\d+')
    pa2=re.compile('\w+@[163|gmail|qq]+\.com')
    pa3=re.compile('<head>[^<]+</head>')
    print pa3.findall(str3)
    #print pa.findall(str)
def qiushibaike():
    content=requests.get('http://www.qiushibaike.com').content
    soup=BeautifulSoup(content,'html.parser')

    for div in soup.find_all('div',{'class':'content'}):
        print div.text
if __name__=='__main__':
    demo_regex()
   #print 'hello world'