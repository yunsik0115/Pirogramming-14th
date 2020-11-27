import numpy as np
import pandas as pd

col = ['국가', '인구 수', '감염자 수']
ind = ['한국', '중국', '일본', '미국', '독일']
con = [[1500, 300], [3000, 800], [2000, 500], [2500, 750], [2200, 1000]]


while True:
    print('''
    -------------------
       코로나 종식 게임   
    -------------------
    1. 백신 정보
    2. 감염된 국가 정보
    3. 게임 시작
    4. 게임 종료
    ''')

    choice = int(input())

    if choice == 1:
        print("벡신 정보 출력")
    elif choice == 2:
        print("감염 국가 정보 출력")
    elif choice == 3:
        print("게임시작")
    elif choice == 4:
        print("게임을 종료합니다")
        break
