num = 0 # 숫자변수 : 0이 아니면 True
if num: # 변수
    print(num)
else:
    print('not num')

if not num: # !False -> True
    print('not num2')

score = 70 # score -> stack / 70 -> heap 에 저장
# 참조 : reference -> 참조가 0이 되면 heap에 있는 70은 자동으로 garbage collection (메모리 해제)
if score >= 80:
    print("80이상")
else:
    print("80이하")

city = ' ' # null 문자열 => False
# 공백도 문자열이다
if not city:
      print('empty city')

if len(city) > 0:
      print(city)

city = 'incheon'
cities = ['seoul', 'suwon']
# 조건문이 없으면 error
if "ddd" in cities: # 포함연산자
    print(cities.index("ddd"))

# 중첩 if문
score = int(input("점수를 입력하세요: "))
print(f"입력된 점수: {score}")
if score >= 60:
    print("합격입니다!")
    # 경우의 수가 4가지
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    print(f"당신의 등급은 {grade} 입니다.")
else:
    print("불합격입니다.")
    print("다음에 다시 도전하세요!")

print("프로그램 종료")

# 코끼리 연산자 python 3.8부터 사용이 가능함
# 가상공간 virtual machine을 생성 -> 버전차이를 극복
sample_str = "Hello"
if(length := len(sample_str)) >= 5:
    print(f"문자열 길이: {length}")
else:
    print(f"문자열 길이: {length}")

total = 0 # 누적변수
count = 0
count2 = 0
count3 = 0
# range에서 증감값은 1이 default값
for i in range(1,11): # 초기값, 한계값, 증감값
    total += i # total = total + i
    print(i)
    count = i
    # count += 1
    if(i % 2 == 0):
      count2 += i
    if(i % 3 ==0):
      count3 += i
print(f"1부터 10까지의 합계: {total}")

# 문제 : 횟수를 카운트하시오
print(f"총 카운트: {count}")

# 문제 : 2의 배수만 더하시오
print(f"2의 배수 합계: {count2}")

# 문제 : 3의 배수의 합을 계산하시오
print(f"3의 배수 합계: {count3}")

# while문 : 주로 불규칙한 횟수를 지정하는 경우
total = 0 # 초기값
i = 1
while i <= 10: # 한계값 -> 종료조건
    total += i # 처리
    i += 1 # 증감값

print(f"1부터 10까지의 합계(while): {total}")

# sum 함수를 이용한 합계
# sum함수는 c, java에서는 2개의 요소만 입력
# python의 기본 자료구조가 list
total = sum(range(1,11))
print(f"합계: {total}")

# 이것을 이용해서 1부터 10까지의 2의 배수의 합계를 출력하시오
total = sum(range(2,11,2))
print(f"2의 배수 합계: {total}")

# 문제
# 0이 아닌 숫자를 입력받아서 합계를 더하는 프로그램을 작성하시오
# 0이 입력되면 종료됨
total = 0;
while (1): # 무한 루프
  num = int(input("숫자를 입력하세요: "))
  if num == 0 : # 종료조건
    break;
  total += num
print("입력받은 숫자들의 합:", total)


total = 0;
while (num := int(input("숫자를 입력하세요: "))) != 0:
       total += num
print("입력받은 숫자들의 합:", total)

# list comprehension
result = [x for x in range(10)]
# 다음과 같은 수식
# result = []
# for x in range(10):
#     result.append(x)
print(result)

result = [x for x in range(10) if x%2==0]
print(result)

test = [x for x in range(0,10,2)]
print(test)

# 문제 : 0부터 9까지의 제곱값을 구하되, 그 제곱값이 30미만인 경우만 뽑아서 리스트로 생성하시오
result = [x**2 for x in range(10) if x**2 < 30]
print(result)

result = [square for x in range(10) if (square := x**2) < 30]
print(result)

# 삼항연산자
x=5
ans = '양수' if x>=0 else '음수'
# if x>=0:
#   ans = '양수'
# else:
#   '음수'
print(ans)

# is
x = [1,2,3]
y = [1,2,3]

print(x==y)
print(x is y) # 메모리 주소가 같아야 함

a = [1,2]
b = a

print(a == b)
print(a is b)

# 문제 : 두 개의 데이터를 입력받아서 숫자이면 더해서 출력하고
# 아니라면 숫자인지 아닌지 확인해서 출력하시오
# isdigit()

# 변수 작성의 규칙 : 변수이름으로부터 데이트를 추상

data1 = input("첫 번째 데이터 입력: ")
data2 = input("두 번째 데이터 입력: ")

if(data1.isdigit() and data2.isdigit()):
    print(eval(data1) + eval(data2))
elif(data1.isdigit() and not data2.isdigit()):
    print("두 번째 숫자 아님")
elif(not data1.isdigit() and data2.isdigit()):
    print("첫 번째 숫자 아님")
else:
    print("둘 다 숫자 아님")



# 문제 : 수익(income)과 지출(cost)를 입력받아서 순수익을 출력하시오
# 조건
# 수익과 지출이 동일한 경우를 고려하시오(손익분기점)
# 제약조건
# 소수점 2째 자리까지 출력
# 결과에 따라서 순수익과 순지출을 계산해서 출력하시오

income = input("수익 :")
cost = input("지출 :")
# diff = eval(income) - eval(cost)

if((diff := eval(income) - eval(cost)) == 0):
    print(f"손익분기점")
elif(diff < 0):
    print(f"순지출: {abs((round(diff, 2)))}")
else:
    print(f"순수익: {abs((round(diff, 2)))}")

# 아두이노/라즈베리파이(IoT)로 구현된 날씨 표시 시스템의 상태표이다

#         STEADY      FLASHING
# BLUE    화창한 날   구름낀 날
# RED     비오는 날   눈오는 날

# color와 mode를 입력받아서 날씨를 텍스트로 출력하는 프로그램을 작성하시오

color = input("색상: ").upper() # 대문자로 변경
mode = input("모드: ").upper()

if(color == "BLUE"):
    if(mode == "STEADY"):
        print("화창한 날")
    elif(mode == "FLASHING"):
        print("구름낀 날")
    else:
        print("모드 입력 오류")
elif(color == "RED"):
    if(mode == "STEADY"):
        print("비오는 날")
    elif(mode == "FLASHING"):
        print("눈오는 날")
    else:
        print("모드 입력 오류")
else:
    print("색상 입력 오류")

# num1 = eval(input("숫자 입력1 : "))
# num2 = eval(input("숫자 입력2 : "))
# if num1 > num2:
#     largestValue = num1
# else:
#     largestValue = num2
# print("제일 큰 수는 : ", str(largestValue))

# 문제 : 3개의 수를 입력받아서 제일 큰 수를 출력하시오
num1 = eval(input("숫자 입력1 : "))
num2 = eval(input("숫자 입력2 : "))
num3 = eval(input("숫자 입력3 : "))

# if num1 > num2:
#     if num1 > num3:
#         largestValue = num1
#     else:
#         largestValue = num3
# else:
#     if num2 > num3:
#         largestValue = num2
#     else:
#         largestValue = num3

largestValue = num1
if num2 > largestValue:
    largestValue = num2
if num3 > largestValue:
    largestValue = num3

# largestValue = max(num1, num2, num3)

print("제일 큰 수: ", largestValue)

# 과일 100.50 원에 세금 12.5%를 붙여서 팔았다
# 세금과 매출액이 얼마인지 출력하시오
# 소수점 2째 자리까지 표현하시오

tax = 100.50 * (12.5/100)
price = 100.50 + tax

print(f"세금: {round(tax, 2) } / 매출액: {round(price, 2)}")

# 일 수를 입력해서 초로 변경하는 프로그램 작성
day = eval(input("일 수를 입력하세요: "))
second = day*24*60*60

print(f"{second} 초")

#Optimization(최적화 -> 속도, 성능 향상을 위해서 코드 단축? 압축?)
# 놀이 공원 매표소 단체 입장료 계산하기
# 조건
# 1. 팀별 인원 구성을 입력 (초등학생, 청소년, 일반인, 경로대상)
# 2. 정산요금 - 초등학생(5000원) / 청소년(10000원) / 일반인(15000원) / 경로대상(3000원)
# 팀별할인 카드 확인
# 카드없음 : 할인 무 / 일반카드 : 10% / VIP카드 : 20%
# 카드 숫자로 매핑 - 카드 없음 : 0 / 일반 : 1 / VIP : 2
# 총입장료를 출력하시오

# 상수확인 -> 상수를 변수화
age1_price = 5000
age2_price = 10000
age3_price = 15000
age4_price = 3000

age1 = int(input("초등학생 수: "))
age2 = int(input("청소년 수: "))
age3 = int(input("일반인 수: "))
age4 = int(input("경로대상 수: "))

card = int(input("할인카드 종류: "))

sum = age1 * age1_price + age2 * age2_price + age3 * age3_price + age4 * age4_price

if(card == 0):
    result = sum
elif(card == 1):
    result = sum * 0.9
elif(card == 2):
    result = sum * 0.8

print(f"총 입장료 : {int(result)}원")

# 아래와 같은 형태로 줄일 수 있음
# select = [tot, tot*0.9, tot*0.8]
# print("총 요금은", select[dis], "원 입니다.")

# 주말과제
# 소득을 입력하면 세율표에 의해서 세금 계산해서 출력
# https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&cntntsId=7667
# 제출형식
# 날짜_이름_주제.ipnb

tax_1 = [0.06, 0]
tax_2 = [0.15, 1260000]
tax_3 = [0.24, 5760000]
tax_4 = [0.35, 15440000]
tax_5 = [0.38, 19940000]
tax_6 = [0.40, 25940000]
tax_7 = [0.42, 35940000]
tax_8 = [0.45, 65940000]

income = int(input("소득을 입력하세요: "))

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

print(f"세금: {round(tax)}원")



elements = ["earth", "air", "fire", "water"]
for i in elements:
    print(i, end = " ")
# range를 이용해서 출력해 보시오
for i in range(len(elements)):
    print(elements[i], end = " ")

# 데이터 타입 이름은 변수로 사용하면 안됨
# list = [1,2,3]
print(list(range(10)))
print(list(range(1,10)))
print(list(range(10,0,-1)))
print(list(range(1,10,2)))

print(reversed(range(10)))
print(list(reversed(range(10))))
print(range(5, -1, -1))
print(list(range(5, -1, -1)))

# iterator
ra=range(10)
ra=iter(ra) # iterator 객체를 생성

next(ra, "끝") # 메모리를 효율적으로 사용가능

# generator
def simpleGeneratorFun(): # 데이터 생성함수
    # 주로 while문과 활용
    yield 1 # 실행을 멈춤
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)

# zip -> 따로 있는 데이터 리스트를 매칭해서 하나의 리스트로 생성
seq1 = ['a', 'b', 'c']
seq2 = [10, 20]
zipped = zip(seq1, seq2)
list(zipped)

# 문제
# 1부터 30까지는 홀수, 30부터 60까지는 짝수 출력
for i in range(1, 61):
    if(i <= 30):
        if(i%2 == 1):
          print(i, end=" ")
    else:
        if(i%2 == 0):
          print(i, end=" ")

# for x in range(1,11):
#   print()
#   for y in range(1,11):
#     print(y, end=" ")
# 90도 돌려서 출력하시오
for x in range(1,11):
  print()
  for y in range(1,11):
    print(x, end=" ")

# 구구단을 생성하시오
for x in range(1,10):
  print()
  for y in range(1,10):
    print(f"{y} * {x} = {x*y}", '\t', end=" ")

# \n new line, \t tab 일정한 거리를 띄움

# 저장용량
# 1byte = 8bit = 256
# 2**10 = 1024 = 1kb
# 1024kb = 1mb
# 1024mb = 1gb
# 1024gb = 1tb

# 문제 : 용량을 입력하고 이를 바이트로 계산하는 프로그램을 작성하시오
# 입력방식은 250 G (공백으로 분리해서 단위를 입력하시오)
# 문자열 분리 : split
# 용량이 대문자, 소문자를 확인하기 위해 upper 사용

UNIT = 1024
volumein = input("용량을 입력하시오(입력방식 250 M(공백분리))")
data_unit = volumein.split(" ")
calc_unit = data_unit[1].upper().strip() # 앞뒤의 공백 제거
volume = int(data_unit[0])
volume_res = 0
if calc_unit == "K":
    volume_res = volume * UNIT
elif calc_unit == "M":
    volume_res = volume * UNIT * UNIT
elif calc_unit == "G":
    volume_res = volume * UNIT * UNIT * UNIT
elif calc_unit == "T":
    volume_res = volume * UNIT * UNIT * UNIT * UNIT
else:
    print("계산 가능한 용량단위가 아니므로 다시 입력하시오")

if volume_res != 0:
  print(f"입력한 용량 {volumein}은 {str(volume_res)}바이트입니다.")

UNIT = 1024

while 1:
  volumein = input("용량을 입력하시오(입력방식 250 M(공백분리))")
  if(volumein.upper() == "Q"):
    break;
  data_unit = volumein.split(" ")
  if(len(data_unit) > 1): # 입력이 있을 때만 작동 제한
    calc_unit = data_unit[1].upper().strip() # 앞뒤의 공백 제거
    volume = int(data_unit[0])
    volume_res = 0
    if calc_unit == "K":
        volume_res = volume * UNIT
    elif calc_unit == "M":
        volume_res = volume * UNIT * UNIT
    elif calc_unit == "G":
        volume_res = volume * UNIT * UNIT * UNIT
    elif calc_unit == "T":
        volume_res = volume * UNIT * UNIT * UNIT * UNIT
    else:
        print("계산 가능한 용량단위가 아니므로 다시 입력하시오")

    if volume_res != 0:
      print(f"입력한 용량 {volumein}은 {str(volume_res)}바이트입니다.")

  else:
    print("형식에 맞추어서 입력하시오")

import sys
import random

while(True):
  print("컴퓨터가 게임을 위해 수를 선택했습니다. ")
  com = random.randint(1, 100) # 뒤의 숫자까지 포함
  count = 0
  while(True):
    person = int(input("숫자를 입력하세요: "))

    if person.upper() == "Q":
      sys.exit(0) # 프로그램 종료

    count += 1

    if com > person:
      print("숫자가 큽니다")
    elif com < person:
      print("숫자가 작습니다")
    else:
      print("정답입니다!")
      break
    if count >= 10:
      break;

# 문제
# 게임이 끝나면 몇전 몇승 몇패 인지 출력하시오

import sys
import random

count = 0
win = 0
lose = 0

while(True):
  tryCount = 0
  com = random.randint(1, 100) # 뒤의 숫자까지 포함
  print("컴퓨터가 게임을 위해 수를 선택했습니다. ")

  while(True):
    person = (input("숫자를 입력하세요: "))

    if person.upper() == "Q":
      print(f"총 {count}전 {win}승 {lose}패 입니다")
      sys.exit() # 프로그램 종료

    person_ans = int(person)
    tryCount += 1

    if com > person_ans:
      print("숫자가 큽니다")
    elif com < person_ans:
      print("숫자가 작습니다")
    else:
      print("정답입니다!")
      win += 1
      break
    if tryCount >= 10:
      lose += 1
      print("패배ㅜㅜ")
      break

  count += 1

def test_generator():
	yield 1 # 값을 리턴하면서 함수 실행을 멈추고 상태를 기억
	yield 2
	yield 3
gen = test_generator()

next(test_generator())