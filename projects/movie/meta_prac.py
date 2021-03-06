import requests
from bs4 import BeautifulSoup

url = 'https://www.goodchoice.kr/product/detail?ano=69906&adcno=2&sel_date=2022-06-26&sel_date2=2022-06-27'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.

image = soup.select_one('meta[property="og:image"]')['content']
title = soup.select_one('meta[property="og:title"]')['content']
description = soup.select_one('meta[property="og:description"]')['content']

print(image)
print(title)
print(description)
