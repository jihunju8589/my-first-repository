import requests
from bs4 import BeautifulSoup

res = requests.get("http://v.media.daum.net/v/20170518153405933")
soup = BeautifulSoup(res.content, "html5lib")

print(soup.find_all(string="오대석"))
print(soup.find_all(string=["[이주의해시태그-#네이버-클로바]쑥쑥 크는 네이버 AI", "오대석"]))
print(soup.find_all(string="AI"))
# print(soup.find_all(string=re.compile("AI"))[0])
# print (soup.find_all(string=re.compile('AI')))
