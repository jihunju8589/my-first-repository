import requests
from bs4 import BeautifulSoup
from pprint import pprint
res=requests.get('https://comic.naver.com/webtoon/weekday.nhn')
soup=BeautifulSoup(res.content, 'html.parser')
data1=soup.find("div", {"class": "list_area daily_all"})

for i in range(0,7):
    today=data1.find_all("div", {"class": "col"})[i]
    today_data=today.findAll("a", {"class": "title"})
    today_list=[t.text for t in today_data]
    pprint(today_list)

