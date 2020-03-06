import requests
from bs4 import BeautifulSoup

datas = [
    "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=081&aid=0003070258",
    "https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=079&aid=0003330636&date=20200303&type=1&rankingSeq=1&rankingSectionId=103",
    "https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=081&aid=0003070158&date=20200303&type=1&rankingSeq=4&rankingSectionId=100",
    "https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=052&aid=0001409067&date=20200303&type=2&rankingSeq=1&rankingSectionId=104",
]

for data in datas:
    res = requests.get(data)
    soup = BeautifulSoup(res.content, "html.parser")

    title = soup.find("h3", id="articleTitle")
    date = soup.find("span", "t11")

    print("기사 제목: {0}".format(title.get_text()))
    print("기사 작성일: {0}".format(date.get_text()))


# h3 태그, id = articleTitle, class = tts_head
# span 태그, class = t11
