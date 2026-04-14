# 주말과제
# 소득을 입력하면 세율표에 의해서 세금 계산해서 출력
# https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&cntntsId=7667
# 제출형식
# 날짜_이름_주제.ipnb

# 소득세 세율 및 누진공세 list
# [세율, 누진공제]
tax_1 = [0.06, 0]
tax_2 = [0.15, 1260000]
tax_3 = [0.24, 5760000]
tax_4 = [0.35, 15440000]
tax_5 = [0.38, 19940000]
tax_6 = [0.40, 25940000]
tax_7 = [0.42, 35940000]
tax_8 = [0.45, 65940000]

# 입력값 계산 위해서 int로 변환
income = int(input("소득을 입력하세요: "))

# 과세표준 범위 계산
if(income <= 14000000):
    tax = income * tax_1[0] - tax_1[1]
elif(14000000 < income <= 50000000):
    tax = income * tax_2[0] - tax_2[1]
elif(50000000 < income <= 88000000):
    tax = income * tax_3[0] - tax_3[1]
elif(88000000 < income <= 150000000):
    tax = income * tax_4[0] - tax_4[1]
elif(150000000 < income <= 300000000):
    tax = income * tax_5[0] - tax_5[1]
elif(300000000 < income <= 500000000):
    tax = income * tax_6[0] - tax_6[1]
elif(500000000 < income <= 1000000000):
    tax = income * tax_7[0] - tax_7[1]
else:
    tax = income * tax_8[0] - tax_8[1]

# 돈이기 때문에 정수로 반올림
tax_int = round(tax)
# :, 사용하면 자동으로 숫자에 천원단위로 콤마찍힘
print(f"세금: {tax_int:,}원")

# 문제
# 게임이 끝나면 몇전 몇승 몇패 인지 출력하시오

import sys
import random

count = 0 # 게임 횟수
win = 0 # 승리 횟수
lose = 0 # 패배 횟수

while (True):
  tryCount = 0 # 한 게임 내에서 시도 횟수
  com = random.randint(1, 100) # 뒤의 숫자까지 포함
  print("컴퓨터가 게임을 위해 수를 선택했습니다. ")

  while (True):
    person = input("숫자를 입력하세요 (Q: 종료): ")

    # Q를 입력해서 종료할 경우
    if person.upper() == "Q":
      print(f"총 {count}전 {win}승 {lose}패 입니다") # 전적 출력
      sys.exit() # 프로그램 종료

    # 입력값 검증
    # 1. 숫자 체크
    if person.strip().isdigit():
      person_ans = int(person)
      # 2. 범위(1 ~ 100) 체크
      # 범위에 벗어나 있으면 경고문 출력 후 다시 진행
      if not (1 <= person_ans <= 100):
        print("1~100 사이의 숫자를 입력하세요")
        continue
    # 숫자가 아닐 경우 -> 경고 안내문 출력 후 다시 진행
    else:
      print("유효한 숫자를 입력하거나 Q를 눌러 종료하세요")
      continue

    # 위에 조건 통과했을 경우(올바른 값을 입력했을 경우)
    # 시도 횟수 카운팅 및 다음 단계 진행
    tryCount += 1

    if com > person_ans:
      print("숫자가 큽니다")
    elif com < person_ans:
      print("숫자가 작습니다")
    # 정답일 경우 승리 횟수 카운팅 및 현재 게임 종료
    else:
      print("정답입니다!")
      win += 1
      break

    # 10번 시도했을 경우 -> 패배처리
    # 패배 횟수 카운팅 및 현재 게임 종료
    if tryCount >= 10:
      lose += 1
      print(f"패배ㅜㅜ 정답은 {com}")
      break

  # 한 판이 올바르게 끝났을 경우에만 게임 횟수 카운팅
  count += 1