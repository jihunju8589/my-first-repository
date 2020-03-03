import requests
from bs4 import BeautifulSoup

target = requests.get("http://v.media.daum.net/v/20170615203441266")  # 크롤링할 타겟 주소
soup = BeautifulSoup(target.content, "html.parser")  # 타겟을 html.parser로 해석한 객체 만듬
print(soup)
title = soup.find("title")  # soup 객체 안에 title이라는 속성을 찾음

print(title.get_text())  # title을 읽어와서 출력함
