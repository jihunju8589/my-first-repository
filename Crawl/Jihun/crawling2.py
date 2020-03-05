import requests
from bs4 import BeautifulSoup
from pprint import pprint
# res=requests.get('https://comic.naver.com/webtoon/weekday.nhn')
# soup=BeautifulSoup(res.content, 'html.parser')
# data1=soup.find("div", {"class": "col"})
# data2=data1.findAll("a", {"class": "title"})
# mon_list=[]
# for i in data2:
#     mon_list.append(i.text)
# pprint(mon_list)

res=requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup=BeautifulSoup(res.content, 'html.parser')
data3=soup.find("div", {"class": "col col_selected"})
data4=data3.findAll("a", {"class": "title"})
tue_list=[]
for i in data4:
    tue_list.append(i.text)
pprint(tue_list)

