import requests
from bs4 import BeautifulSoup

html = """
<h1>주지훈</h1>
<h2>주지훈주지훈</h2>
"""

soup = BeautifulSoup(html, "html.parser")

# 태그로 검색 방법
title_data = soup.find("h2")

print(title_data)
print(title_data.string)
print(title_data.get_text())
