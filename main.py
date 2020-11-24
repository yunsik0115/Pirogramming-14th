import random
from operator import itemgetter

category = ["한국", 300]

class GameImpl:
    def cure(nation, vaccine_n):
        """사용자 선택 백신, 국가번호에 따라 적용하여, 해당 국가 감염자수 수정"""

    def InfectIncrease(nation):
        """라운드마다 해당 국가 인구수 15%만큼 감염자수 증가"""

    def Shuffle():
        """백신과 국가에 대한 정보 섞는 함수"""

    def printResult():
        """백신 투여 후 결과 출력 함수"""

    def printScore():
        """최종 스코어 출력 함수"""


while True:
    print('''
      ---------------------
          코로나 종식 게임
      ---------------------
        1. 백신 정보
        2. 감염된 국가 정보
        3. 게임 시작
        4. 게임 종료
        
    ''')

    choice = int(input())

    if choice == 1 :
        print('A')
    elif choice == 2:
        print('B')
    elif choice == 3:
        print('C')
    elif choice == 4:
        print('게임을 종료합니다')
        break

