#小说url在https://www.qu.la/ 里添加

import requests
import  re
url="https://www.qu.la/book/39775/"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
response=requests.get(url, headers=headers)
response.encoding='utf-8'
#提取网页的html信息
html=response.text
#获取小说的名字
title=re.findall(r'<h1>(.*?)</h1>',html)[0]
#print(title)
#新建一个txt文件保存小说
fb=open('%s.txt'%title,'w',encoding='utf-8')
#获取每一章的信息和url
dl=re.findall(r'dt>.*</dt>(.*?)</dl>',html,re.S)[0]
#print(dl)
chapter_list_info=re.findall(r'<a style="" href="(.*?)">(.*?)</a></dd>',dl)
#print(chapter_list_info)

#循环章节下载
for chapter_info in chapter_list_info:
    # chapter_title=chapter_info[1]
    # chapter_url=chapter_info[0]
    chapter_url,chapter_title=chapter_info
    chapter_url="https://www.qu.la%s" %chapter_url
    #下载章节内容
    chapter_response=requests.get(chapter_url,headers=headers)
    chapter_response.encoding='utf-8'
    chapter_html=chapter_response.text
    #获取小说章节的文本内容
    chapter_text= re.findall(r'<div id="content">(.*?)<script>chaptererror', chapter_html, re.S)[0]
    #清洗小说内容
    chapter_text=chapter_text.replace(" ","")
    chapter_text = chapter_text.replace("&nbsp;", "")
    chapter_text = chapter_text.replace("<br/>","")
    chapter_text = chapter_text.replace("</br>","")


    #保存小说章节内容
    fb.write(chapter_title)
    fb.write(chapter_text)
    print(chapter_url)
