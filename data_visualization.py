from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

browser = webdriver.Chrome()
url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"

browser.get(url)

html = browser.page_source #Browser상의 브라우저 정보의 HTML소스 가져옴
soup = BeautifulSoup(html, 'html.parser') # soup를 통해 문서 해석 및 데이터 추출 가능

channel_list = soup.select('form > table > tbody > tr')
print(len(channel_list), '\n')
print(channel_list[0])

channel = channel_list[0]
print(channel)

category = channel.select('p.category')[0].text.strip()
print(category)

title = channel.select('h1 > a')[0].text.strip()
print(title)

subscriber = channel.select('.subscriber_cnt')[0].text
view = channel.select('.view_cnt')[0].text
video = channel.select('.video_cnt')[0].text

print(subscriber)
print(view)
print(video)