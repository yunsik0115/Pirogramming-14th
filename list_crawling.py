from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

executable_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=executable_path)

url = 'https://www.melon.com/chart/index.htm'

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

tags_span = soup.select('span')
tags_p = soup.select('p')

songs = soup.select('table > tbody > tr')
song_data = []
rank = 1

for song in songs:
    title = song.select('div.ellipsis.rank01 > span > a')[0].text
    singer = song.select('div.ellipsis.rank02 > a')[0].text
    song_data.append(['Melon', rank, title, singer])
    rank = rank + 1


#songs = driver.find_element_by_css_selector('table >tbody > tr')
#for song in songs:
#    title = song.find_element_by_css_selector('div.ellipsis.rank01 > span > a')[0].text
#    singer = song.find_element_by_css_selector('div.ellipsis.rank02 > a')[0].text
#    print(title, singer, sep='|') // via selenium

columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
pd_data.head()



output_file = 'my_file.xlsx'
output_dir = Path('long_path/to/my_dir')

output_dir.mkdir(parents=True, exist_ok=True)

# 존재하지 않는 경로일 경우 상단 설정 필요.

pd_data.to_excel(output_dir / output_file)