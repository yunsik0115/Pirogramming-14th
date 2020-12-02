import random
import numpy as np
import pandas as pd
import itertools
import time


class Services:
    nation_col = ['인구 수', '감염자 수']
    nation_ind = ['1. 한국', '2. 중국', '3. 일본', '4. 미국', '5. 독일']
    nation_con = [[1500, 300], [3000, 800], [2000, 500], [2500, 750], [2200, 1000]]
    nation_table = pd.DataFrame(nation_con, columns=nation_col, index=nation_ind)
    """인덱스 0 -> 인구수 인덱스 1 -> 감염자 수"""

    vac_col = ['백신치료율(단위 %)']
    vac_ind = ['백신 1', '백신 2', '백신 3']
    vac_con = [25, 50, 100]
    vac_table = pd.DataFrame(vac_con, columns=vac_col, index=vac_ind)

    round = 0

    def print_vac(self):
        print("========백신 목록=========")
        print(self.vac_table)
        print("======목록 출력 종료=======")

    def cure(self, nation, vaccine):
        self.nation_table.at[nation-1, 1] -= (self.nation_table.iloc[nation-1, 1]) \
                                          * (self.vac_table.iloc[vaccine-1, 0]) * 0.01

    def infection_increase(self, nation):
        self.nation_table.at[nation-1, 1] += (self.nation_table.iloc[nation, 1]) * 0.15
        self.round += 1

    def is_finished(self):
        index = 0
        while index < 5:
            if self.nation_table.iloc[index, 0] < self.nation_table.iloc[index, 1]:
                print("감염자수가 인구수보다 증가함에 따라 게임을 종료합니다")
                self.print_score()
                exit(0)
                index += 1
        if self.round > 5:
            print("5라운드까지 모두 종료되었습니다. 결과를 출력합니다")
            self.print_score()
            exit(0)

    def print_result(self):
        if self.round != 0:
            print("============================================")
            print(self.round, '차백신투여 후 감염된 나라에 대한 정보===')
            print("============================================")
        print(self.nation_table)

    def print_score(self):
        print("=======최종 스코어=======")
        final_score = self.nation_table.sort_values(by='감염자 수', ascending=True)
        print(final_score)
        print("========출력 종료========")

    def shuffle(self, target_table):
        self.nation_table = self.nation_table.sample(frac=1).reset_index(drop=True)
        self.round = 0


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
    Service = Services()
    choice = int(input())

    if choice == 1:
        Service.print_vac()
        time.sleep(5)
    elif choice == 2:
        Service.print_result()
        time.sleep(5)
    elif choice == 3:
        print("사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 입력하세요")
        vaccine_choice = list(map(int, input("백신 선택(1~3)").split()))
        nation_choice = list(map(int, input("국가 선택(1~5)").split()))
        vaccine_choice = vaccine_choice + [0]*(5-len(vaccine_choice))
        i = 0
        while i < 5:
            Service.is_finished()
            Service.cure(vaccine_choice[i], nation_choice[i])
            Service.infection_increase(nation_choice[i])
            Service.print_result()
            i += 1
    elif choice == 4:
        print("게임을 종료합니다")
        break
