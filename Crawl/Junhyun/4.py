import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.naver.com")
soup = BeautifulSoup(res.content, "html.parser")

title = soup.find("title")  # soup 객체 안에 title이라는 속성을 찾음
print(title.get_text())  # title을 읽어와서 출력함