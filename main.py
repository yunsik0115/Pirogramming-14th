import random
from operator import itemgetter

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
        print("A")
    elif choice == 2:
        print("B")
    elif choice == 3:
        print("C")
    elif choice == 4:
        print("게임을 종료합니다")
        break

