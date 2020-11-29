import random
import numpy as np
import pandas as pd
from pandas import DataFrame

class services:
    nation_col = ['인구 수', '감염자 수']
    nation_ind = ['한국', '중국', '일본', '미국', '독일']
    nation_con = [[1500, 300], [3000, 800], [2000, 500], [2500, 750], [2200, 1000]]
    nation_table = pd.DataFrame(nation_con, columns=nation_col, index=nation_ind)
    """인덱스 0 -> 인구수 인덱스 1 -> 감염자 수"""

    vac_col = ['치료율(단위 %)']
    vac_ind = ['백신1', '백신2', '백신3']
    vac_con = [25, 50, 100]
    vac_table = pd.DataFrame(vac_con, columns=vac_col, index=vac_con)


    def infectionIncrease(self, nation_choice):
        self.nation_table
    def printResult(self):
        print(self.nation_table)
    def printScore(self):
        print(nation_table)
    def shuffle(self, target_table):
        self.nation_table = self.nation_table.sample(frac = 1)


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
    service = services()
    choice = int(input())

    if choice == 1:
        print("벡신 정보 출력")
    elif choice == 2:
        print("===감염 국가 정보 출력===")
        service.printResult()
        print("=======출력==종료=======")
    elif choice == 3:
        print("사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 입력하세요")
        print("사용할 백신 선택 :" )
        vaccine_choice = (int(input()))
        print("국가 번호 입력 :")
        nation_choice = (int(input()))
    elif choice == 4:
        print("게임을 종료합니다")
        break
