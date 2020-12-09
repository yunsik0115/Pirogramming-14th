import pandas as pd
import random
import time


class Services:
    nation_col = ['인구 수', '감염자 수']
    nation_ind = ['한국', '중국', '일본', '미국', '독일']
    nation_con = [[1500, 300], [3000, 800], [2000, 500], [2500, 750], [2200, 1000]]
    nation_table = pd.DataFrame(nation_con, columns=nation_col, index=nation_ind)

    vac_col = ['백신치료율(단위 %)']
    vac_ind = ['백신 1', '백신 2', '백신 3']
    vac_con = [25, 50, 100]
    vac_table = pd.DataFrame(vac_con, columns=vac_col, index=vac_ind)
    round = 0

    cured = 0
    add_infection = 0

    def print_vac(self):
        print("========백신 목록=========")
        print(self.vac_table)

    def cure(self, nation, vaccine):
        print("\n\n\n★", self.round + 1, "번째 시도★")
        print("=============선택된 백신 정보=============\n",
              self.vac_table.iloc[[vaccine - 1]])
        print("=============선택된 국가 정보=============\n",
              self.nation_table.iloc[[nation - 1]])
        self.cured += int((self.nation_table.iloc[nation - 1, 1] * (self.vac_table.iloc[vaccine - 1, 0] * 0.01)))
        self.nation_table.iloc[nation - 1, 1] = \
            int(self.nation_table.iloc[nation - 1, 1] * (1 - self.vac_table.iloc[vaccine - 1, 0] * 0.01))

    def infection_increase(self):
        inf_index = 0
        while inf_index < 5:
            self.add_infection += int(self.nation_table.iloc[inf_index, 1] * 0.15)
            self.nation_table.iloc[inf_index, 1] += int(self.nation_table.iloc[inf_index, 1] * 0.15)
            inf_index += 1
        self.round += 1

    def is_finished(self):
        is_index = 0
        while is_index < 5:
            if self.nation_table.iloc[is_index, 0] < self.nation_table.iloc[is_index, 1]:
                print("감염자수가 인구수보다 증가함에 따라 게임을 종료합니다")
                self.print_score()
                return True
            is_index += 1

        if self.round > 4:
            print("\n\n\n5라운드까지 모두 종료되었습니다. 결과를 출력합니다")
            self.print_score()
            return True

    def print_result(self):
        if self.round != 0:
            pr_index = 0
            print("============================================")
            print(" ", self.round, '차백신투여 후 감염된 나라에 대한 정보')
            print("============================================")
            while pr_index < 5:
                if pr_index == 0:
                    print("------------완치된 국가 정보------------")
                if self.nation_table.iloc[pr_index, 1] == 0:
                    print(self.nation_table.iloc[[pr_index]])
                pr_index += 1
        print("========감염 국가 목록=========")
        print(self.nation_table[(self.nation_table['감염자 수'] >= 1)])

    def print_score(self):
        compl_cured = 0
        ind = 0
        while ind < 5:
            if self.nation_table.iloc[ind, 1] == 0:
                compl_cured += 1
            if compl_cured == 5:
                print('''===========================================
                                 모든 국가가 완치되었습니다!!
                         ===========================================''')
            ind += 1
        print("=======최종 스코어=======")
        print("-----------치유된 국가 목록-----------")
        print(self.nation_table[self.nation_table['감염자 수'] == 0])
        print("치유된 사람 수 ==> ", self.cured, "명")
        print("추가 감염자 수 ==> ", self.add_infection, "명")
        print("치유된 국가 수 ==> ", compl_cured)
        final_score = self.nation_table.sort_values(by='감염자 수', ascending=True)
        print(final_score.iloc[0:5])
        print("========출력 종료========")

    def shuffle(self):
        self.nation_table = self.nation_table.sample(frac=1)
        random.shuffle(self.vac_con)
        self.vac_table = pd.DataFrame(self.vac_con, columns=self.vac_col, index=self.vac_ind)


while True:
    print('''
    ----------------------
       코로나 종식 게임   
    ----------------------
    1. 백신 정보
    2. 감염된 국가 정보
    3. 게임 시작
    4. 게임 종료
    ''')
    Service = Services()
    choice = int(input())
    i = 0
    index = 0

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
        nation_choice = int(input("적용할 국가 선택(1~5) : "))
        while True:
            Service.cure(nation_choice, vaccine_choice)
            Service.infection_increase()
            Service.print_result()
            ch = Service.is_finished()
            Service.shuffle()
            if ch:
                time.sleep(3)
                exit(0)
            vaccine_choice = random.randint(1, 3)
            while True:
                nation_choice = random.randint(1, 5)
                if Service.nation_table.iloc[nation_choice - 1, 1] != 0:
                    break
    elif choice == 4:
        print("게임을 종료합니다")
        exit(0)