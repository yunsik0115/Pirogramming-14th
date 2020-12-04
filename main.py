import pandas as pd
import time

nation_col = ['인구 수', '감염자 수']
nation_ind = ['1. 한국', '2. 중국', '3. 일본', '4. 미국', '5. 독일']
nation_con = [[1500, 300], [3000, 800], [2000, 500], [2500, 750], [2200, 1000]]
nation_table = pd.DataFrame(nation_con, columns=nation_col, index=nation_ind)
nation_table.con.astype(int)

vac_col = ['백신치료율(단위 %)']
vac_ind = ['백신 1', '백신 2', '백신 3']
vac_con = [25, 50, 100]
vac_table = pd.DataFrame(vac_con, columns=vac_col, index=vac_ind)


class Services:
    round = 0

    def print_vac(self):
        print("========백신 목록=========")
        print(vac_table)

    def cure(self, nation, vaccine):
        print("★", self.round + 1, "번째 시도★")
        print("=============선택된 백신 정보=============\n",
              vac_table.iloc[[vaccine - 1]])
        print("=============선택된 국가 정보=============\n",
              nation_table.iloc[[nation - 1]])
        nation_table.iloc[nation - 1, 1] *= (1 - vac_table.iloc[vaccine - 1, 0] * 0.01)

    def infection_increase(self, nation):
        index = 0
        while index < 5:
            if nation == index:
                continue
            nation_table.iloc[index, 1] += nation_table.iloc[index, 1] * 0.25
            index += 1
        self.round += 1

    def is_finished(self):
        index = 0
        while index < 5:
            if nation_table.iloc[index, 0] < nation_table.iloc[index, 1]:
                print("감염자수가 인구수보다 증가함에 따라 게임을 종료합니다")
                self.print_score()
                return 1
            index += 1

        if self.round > 4:
            print("5라운드까지 모두 종료되었습니다. 결과를 출력합니다")
            self.print_score()
            return 1

    def print_result(self):
        if self.round != 0:
            print("============================================")
            print(self.round, '차백신투여 후 감염된 나라에 대한 정보')
            print("============================================")
        print("========국가 목록=========\n", nation_table, "\n")

    def print_score(self):
        print("=======최종 스코어=======")
        final_score = nation_table.sort_values(by='감염자 수', ascending=True)
        print(final_score)
        print("========출력 종료========")

    def shuffle(self):
        nation_table.sample(frac=1).reset_index(drop=True)
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
    i = 0

    if choice == 1:
        Service.print_vac()
        time.sleep(5)
    elif choice == 2:
        Service.print_result()
        time.sleep(5)
    elif choice == 3:
        print("사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 입력하세요\n"
              "라운드는 5회 진행합니다.")
        Service.print_vac()
        Service.print_result()
        vaccine_choice = int(input("사용할 백신 선택(1~3) : "))
        nation_choice = list(map(int, input("국가 선택(0또는 미입력시 랜덤) : ").split()))
        nation_choice = nation_choice + [0] * (5 - len(nation_choice))
        while True:
            Service.cure(nation_choice[i], vaccine_choice)
            Service.infection_increase(nation_choice[i])
            Service.print_result()
            ch = Service.is_finished()
            if ch == 1:
                break
            time.sleep(3)
            i += 1
    elif choice == 4:
        print("게임을 종료합니다")
        break
