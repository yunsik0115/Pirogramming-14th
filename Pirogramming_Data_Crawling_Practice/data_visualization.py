from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform
import time
import pandas as pd
from pathlib import Path
import os

browser = webdriver.Chrome()

results = []

if platform.system() == 'Windows':
    path = 'c:\Windows\Fonts\malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family= font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    print('Check Your OS System')

for page in range(1,2):
    url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}"
    print(url)

    browser.get(url)

    html = browser.page_source  # Browser상의 브라우저 정보의 HTML소스 가져옴
    soup = BeautifulSoup(html, 'html.parser')  # soup를 통해 문서 해석 및 데이터 추출 가능

    channel_list = soup.select('form > table > tbody > tr')

    for channel in channel_list:
        category = channel.select('p.category')[0].text.strip()
        title = channel.select('h1 > a')[0].text.strip()
        subscriber = channel.select('.subscriber_cnt')[0].text
        view = channel.select('.view_cnt')[0].text
        video = channel.select('.video_cnt')[0].text
        data = [title, category, subscriber, view, video]
        results.append(data)

df = pd.DataFrame(results)
df.columns = ['title', 'category', 'subscriber', 'view', 'video']

output_file = 'youtube_rank.xlsx'
output_dir = Path('long_path/to/my_dir')
output_dir.mkdir(parents=True, exist_ok=True)

df.to_excel(output_dir/output_file)

df = pd.read_excel(output_dir/output_file)
df.head()

df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
df.info()

pivot_df = df.pivot_table(index='category', values='replaced_subscriber', aggfunc=['sum', 'count'])
pivot_df.head()
pivot_df.columns = ['subscriber_sum', 'category_count']
pivot_df.head()

pivot_df.reset_index()

pivot_df = pivot_df.sort_values(by='subscriber_sum', ascending=False)
print(pivot_df)
pivot_df = pivot_df.reset_index()
plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='%1.11f%%')
plt.show()