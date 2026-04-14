a=10
b=20
result = a+b
print(result)

def addvalue(a,b):
  return a+b

print(addvalue(10,20))
print(addvalue(30,40))

# 함수의 매개변수와 리턴값의 타입을 지정하지 않음
# 오버로딩
# C나 java
# C에서는 타입마다 함수를 재작성
# int addvalue(int a,int b):
#   return a+b
# float addvalue_float(float a,float b):
#   return a+b
#
# C++과 자바에서 overloading
# 함수 이름이 다른 것을 해결
# 함수 이름은 같되 매개변수의 타입이 다르거나 개수가 다르면 다른 함수로 인식
# 파이썬에서는 데이터타입을 지정하지 않기 때문에 오버로딩이 자동 해결
# 개수가 다른 것은 default 매개변수로 해결
print(addvalue([10,20,30], [30,40,50]))
print(addvalue("abc","def"))
print(addvalue("내일의", " 희망"))

# default 매개변수는 뒤에 선언되어야 함
# 순서대로 지정
# 매개변수로 선언된 개수와 실매개변수의 개수가 일치해야 함
def reg(x, a=10,b=30):
  return a*x + b
reg(10,30,100)
reg(10,30)
reg(100)

# 파이썬에서는 오버로딩하면 안됨 (같은 이름으로 함수를 선언하면 안됨)
# 뒤에 선언된 함수가 우선시됨
def reg(x):
  a=2
  b=3
  return a*x+b
reg(100)

jumsu=int(input("점수를 입력하시오"))
if jumsu >= 90: print('A')
elif jumsu >= 80: print('B')
elif jumsu >= 70: print('C')
elif jumsu >= 60: print('D')
else: print('F')

# 사용자 정의 함수
# 중복 방지 - 컴퓨터 프로그램은 함수 베이스로 동작
def hakjum_select(jumsu):
  if jumsu >= 90: hakjum='A'
  elif jumsu >= 80: hakjum='B'
  elif jumsu >= 70: hakjum='C'
  elif jumsu >= 60: hakjum='D'
  else: hakjum='F'
  return hakjum
hakjum_select(70)
# 파이썬의 함수는 객체다
# 변수에 대입, 매개변수 전달, 리턴값으로 가능
hakjum_select(int(input("점수를 입력하시오")))

# 파이썬의 함수는 멀티 리턴이 가능
a=10
b=20
def swap(x,y):
  return y,x # tuple로 리턴 - 수정이 불가능
a1,b1 = swap(b,a)
a1,b1

def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
print('시작')
print('add의 결과 : ',add(10,20))
addition = add # 함수를 변수에 대입 (괄호를 지정하지 않음)
# 함수의 주소가 addition 변수에 대입
print('addition의 결과 : ', addition(10,20))
def changefun(g, a, b): # g는 함수다
  return g(a,b) # 함수 호출
# 함수의 실행과 함수의 전달은 다른 의미
# 함수 이름에 ()를 사용하지 않으면 주소 전달
print('결과 : ', changefun(add, 10, 20))
print('결과 : ', changefun(divide, 10, 20))


# keyword parameter
def func_test2(a, b=0, c=3):
  print(a, b)
func_test2(1)
func_test2(1,2)
func_test2(b=2, a=1) # 순서를 변경
func_test2(10, c=3)

# 팀 프로젝트에서 변수 이름과 함수 이름을 통일
def func_test4(): # 에러 나지 않음
  pass

result = func_test4() # None 객체
result is None # is는 객체 비교

# 상속 : 파이썬의 모든 객체는 object를 상속
result.__class__ # 속성 : 부모의 속성 (object)

# call by reference & call by value
# call by reference 는 원래 데이터에 영향을 미침
# call : 함수 호출
# 파이썬은 기본적으로 call by reference로 작동
# 함수가 사용하는 모든 변수는 함수 실행영역인 stack 저장
def changeme(mylist): # 지역변수는 소멸
  # mylist=[1,2,3,4] 대입이 벌어지면 원래의 데이터에 영향을 끼치지 않음
  mylist.append([1,2,3,4]); # 모양유지
  print("함수 내부에서 출력 : ", mylist)
  return

# 파이썬의 리스트는 동적배열이라 추가 삭제 가능
mylist = [10,20,30];
changeme(mylist); # 주소가 전달
changeme(mylist);
changeme(mylist);
changeme(mylist);
print("함수 외부에서 출력 : ",mylist)

# 변동 매개변수
# *는 list
def func1(*args):
  for i in args:
    print(i, end=',')
  print()
print('시작')
func1(1,2,3)
func1(1,2,3,4,5)

# * : list, ** : dict
# *, ** 의 의미
# 받을 때 : 통째로 받음
# 전달할 때 : 풀어서 전달
def say__hello_then_call(f, *args, **kwargs):
  print(' list 매개변수들 ', args)
  print(' key 매개변수는 ', kwargs)
  print(" 함수를 호출 %s" % f)
  return f(*args, **kwargs) # 변수에 있는 값을 사용

def g(x,y,z=1):
  print(x)
  print(y)
  print(z)
  return (x+y)/z

say__hello_then_call(g,1,2,z=5.0)

# 커링 (Currying)
# 원래 함수를 수정하지 않고 변동해서 매개변수 전
def all_number(x,y):
  return x+y
# 무명함수 -> 유명함수
add_five=lambda y: all_number(5,y) # 변수 -> 상수
print(add_five(10)) # 매개변수가 상수로 fix

from functools import partial
add_five = partial(all_number, 5)
print(add_five(100))

# pow 함수 제작
# 2**10 = 1024
# 덧셈의 항등원
# 10 + 0 = 10
# 곱셈의 항등원
# 10 * 1 = 10
# 행렬의 항등원 - 단위행렬
def power(r, n):
  value = 1
  for i in range(1, n+1):
    value = r*value
  return value
print(power(2,3))

# 재귀호출 (함수가 자기자신을 호출할 때)
def power(r,n):
  if n == 1: # 종료조건
    return r
  else:
    return r * power(r, n-1)
print(power(2,3))
# 함수가 함수를 호출하면 함수가 리턴하기 전까지는 호출함수가 종료하지 못함

# stack에서의 동작
# return 값을 가지고 호출한 곳으로 복귀
# 2
# 2 * 함수
# 2 * 함수

# 4 => 4*3*2*1
def factorial(n):
  sum = 1
  for i in range(n, 1, -1):
    sum *= i
  return sum
factorial(5)

# 문제 factorial을 재귀호출로 구현하시오

def factorial(n):
  if (n <= 0):
    return 1
  return n*factorial(n-1)

print(factorial(5))

# 내부함수 : 함수 안에서 정의된 함수
# 함수 안에서 정의된 변수 : 지역변수
def outer():
  def inner():
    print('inner')
  inner() # 함수 내부에서만 실행가능
outer()

# for in 문 뒤에 올 수 있는 것
# Collections(list, tuple, dict, set))
# iterator
# range
# generator
# zip
# enumerate

# generator (생성기 / 메모리 효율성)
# 난수 발생기 -> 의사(가짜)난수 -> 정해진 수가 나옴
# seed값을 통해 제어
import random
def gaus_dist(n):
  while n > 0:
    yield random.random() # 대기 상태를 만듬
    n-=1
gd = gaus_dist(5) # generator object
print(gd)
for i in gd:
  print(i)

gd = gaus_dist(5)
print(gd)
print(next(gd))
print(next(gd))
print(sum(gd)) # 나머지 3개를 더한 값이 출력 (위에 출력된 두번의 값은 사용되서 제외)

list(gaus_dist(5))

# clouser 클로저
# 내부함수와 마찬가지로 외부함수 안에 내부함수 정의
def make_closer(a):
  b = 10
  def closure():
    print("나는 호출한 함수의 배개변수와 지역변수를 알고 있다. : %d %d" % (a,b))
  return closure # 내부함수 리턴

closure=make_closer(5) # 내부함수 종료가 안됨
# 내부함수가 종료가 안되니까, 외부함수도 종료가 안됨
closure()
closure()

del(closure) # 메모리 주소 해제

# 상태를 분리해서 관리
# 외부함수에서는 이름 종류를 관리
# 내부함수에서는 번호를 관리
# decorator 파이썬은 장식자가 발달되어 있음
def cookbook(name):
  def recipe(no):
    print("%s's 호출번호 .%d" % (name, no))
  return recipe

python_recipe = cookbook('python') # 인스턴스하면서 종류
perl_recipe = cookbook('erl')
python_recipe(1)
perl_recipe(2) # 사용하면서 번호
perl_recipe(3)
perl_recipe(4)
id(python_recipe), id(perl_recipe)

# 순차검색, 선형검색
def linear_search(arr, target):
  for i, value in enumerate(arr):
    if value == target:
      return i # 인덱스, 위치검색
  return -1

data = [5,3,8,1,9] # 정렬이 안된 데이터는 순차 검색
print(linear_search(data, 8))

# 이진검색 : 전제조건 -> 정렬
def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  # 왼쪽과 오른쪽의 크기가 뒤집히는 순간이 종료 조건
  while left <= right:
    mid = (left + right) // 2 # 몫연산자 : 인덱스는 정수
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

data = [1,3,5,7,9]
print(binary_search(data,7))

import bisect
a = [1,1,2,3]
bisect.bisect(a,2)

from bisect import bisect_right, bisect_left
# bisect_left : 처음 4가 나타나는 인덱스
# bisect_right : 4보다 큰 수가 처음 나타나는 인덱스
a = [1,2,3,4,4,8]
x = 4
print(bisect_left(a,x))
print(bisect_right(a,x))

# 함수 list
# 함수도 객체 -> 리스트의 요소로 지정이 가능
# 람다함수를 리스트에 입력하면 유명함수가 됨 (인덱스 접근이 가능)
func_choice = [lambda x, y: x**y, lambda x, y: x/y]
print(func_choice[0](10,2))
print(func_choice[1](10,2))
ch = int(input())
if ch == 0: func_choice[0](10,2)
else: func_choice[1](10,2)
func_choice[ch]

# 문제
# 나이를 입력받아서 짝수인 사람은 "나는 귀중한 사람입니다."
# 홀수인 사람은 "나는 행복한 사람입니다."
def ageText(age):
  if(age % 2 == 0):
    print("나는 귀중한 사람입니다.")
  else:
    print("나는 행복한 사람입니다.")
ageText(int(input("나이를 입력하시오: ")))
# whoami=[lambda : print("나는 귀중한 사람입니다."), lambda : print("나는 행복한 사람입니다.")]
# age = int(input("나이를 입력하시오: "))
# whoami[age%2]()

# 문제
# 2차원 평면에서 두 점 사이의 거리값을 구하는 함수를 작성하시오
# 수학함수는 대수적 함수(+,-,*,/), 초월함수(삼각함수, 로그함수, 지수함수)
# math 라이브러리로 별도로 지정
# math.sqrt(제곱근 함수 / 루트)

import math

# def distance_between_points(a, b):
#   xDiff = abs(a[0]-b[0])
#   yDiff = abs(a[1]-b[1])
#   return math.sqrt(xDiff**2 + yDiff**2)

def distance_between_points(x1,y1,z1,x2,y2,z2):
  xDiff = x1-x2
  yDiff = y1-y2
  zDiff = z1-z2
  return math.sqrt(xDiff**2 + yDiff**2 + zDiff**2)

print(distance_between_points(0,1,1,2,2,3))

# 문제
# 총 근무시간과 시간당 급여를 입력받아 주급을 계산하는 함수를 작성하시오
# 조건 : 주당 40시간이 넘는 시간은 1.5배해서 추가 지급
# 함수의 매개변수는 시간당 급여와 주 업무시간

def weekPay(pay, hour):
  baseTime = 40
  if(hour > baseTime):
    result = (pay*baseTime) + (pay*1.5*(hour-baseTime))
  else:
    result = pay*hour
  return round(result)

earn = weekPay(int(input("시간당 급여를 입력하시오: ")), int(input("총 근무시간을 입력하시오: ")))
print(f"{earn:,}원")

# 문제
# 이자율이 주어졌을 때 기간거치 후의 총액과 이자수익을 출력
# 복리계산 원금과 복리 이자의 합
# 복리계산식 : 원금 * (1 + 0.04) ** 거치기간

def calc(baseAmount, period):
  rate = 0.04
  sumAmount = round(baseAmount * ((1+0.04) ** period))
  income = sumAmount - baseAmount
  return sumAmount, income

def main():
  base = int(input("원금을 입력하시오: "))
  period = int(input("기간을 입력하시오: "))
  (sumAmount, income) = calc(base, period)
  print(f"총액: {sumAmount:,}원, 이자수익: {income:,}원")

main()

# 입력함수, 처리함수, 출력함수, 결합함수로 구분해서 구현하시오
def inputData():
  base = int(input("원금을 입력하시오: "))
  period = int(input("기간을 입력하시오: "))
  return (base, period)

def calc(base, period):
  rate = 0.04
  sum = round(base * ((1+0.04) ** period))
  income = sum - base
  return (sum, income)

def printData(sum, income):
  print(f"총액: {sum:,}원, 이자수익: {income:,}원")

def main():
  (base, period) = inputData()
  (sum, income) = calc(base, period)
  printData(sum, income)

main()

# 문제
# 위의 main 함수를 한 줄로 줄이시오(optimization)

# def main(base, period):
#   printData(calc(base, period)[0], calc(base, period)[1])

# main(int(input("원금을 입력하시오: ")), int(input("기간을 입력하시오: ")))

def main():
  printData(*calc(*inputData()))

main()

# 팀 과제
# 3명의 이름 국어 영어 수학 점수 데이터를 입력받아 하나의 리스트(2차원 리스트)에 저장한 다음
# 각 학생에 대한 총점과 평균을 구하고 3명으로 이루어진
# 반의 총점과 평균을 출력하는 프로그램을 작성하시오(2중 for문 적용)
# 리스트 : 동적으로 메모리를 추가하는 것이 가능하기 때문에
# 총점과 평균을 계산한 후, 기존의 리스트에 추가하면 됨
# 입력 처리 출력의 패턴을 지킬 것
# 평균을 소수점 2째 자리까지 출력
# 출력 형태는
# 이름 국어 영어 수학 총점 평균 학점(A/B/C/D) 등수
# 입출력, 계산함수, 학점함수, 석차함수, 출력함수, main함수로 구성

# 입력함수
def getScore():
  classScore = [] # 반 리스트 []
  for i in range(3):
    name = input("이름: ")
    kor = int(input("국어: "))
    eng = int(input("영어: "))
    math = int(input("수학: "))
    score = [name, kor, eng, math] # <= 학생 한명의 데이터
    classScore.append(score)
  return classScore

# 학생별 총점, 평균 계산함수
def getCalcScore(data):
  for i in range(len(data)):
    sum = data[i][1] + data[i][2] + data[i][3]
    avg = round(sum / 3, 2)
    data[i].append(sum)
    data[i].append(avg)


# 학점함수
def getGrade(data):
  for i in range(len(data)):
    if(data[i][4] >= 270): grade = 'A'
    elif(data[i][4] >= 240): grade = 'B'
    elif(data[i][4] >= 210): grade = 'C'
    else: grade = 'D'
    data[i].append(grade)

# 석차함수
def getRank(data):
  data.sort(key=lambda student:int(student[4]))
  for i in range(len(data)):
    rank = 1
    for j in range(len(data)):
      if(data[i][4] < data[j][4]):
        rank += 1
    data[i].append(rank)

# 반 총점/평균 함수
def getClassScore(data):
  classSum = 0
  for i in range(len(data)):
    classSum += data[i][4]
  classAvg = round(classSum / len(data), 2)

  return (classSum, classAvg)


# 출력함수
def printScore(data, classSum, classAvg):
  print(f"반 총점은 {classSum}점, 평균은 {classAvg}점 입니다.")
  for i in range(len(data)):
    print(f"{data[i][0]} 학생은 반에서 {data[i][7]}등으로 총점: {data[i][4]}점, 평균: {data[i][5]}로 학점은 {data[i][6]}입니다.\n국어: {data[i][1]}점, 영어: {data[i][2]}점, 수학: {data[i][3]}점 입니다.")

def main():
  scoreList = getScore()
  getCalcScore(scoreList)
  getGrade(scoreList)
  getRank(scoreList)
  (classSum, classAvg) = getClassScore(scoreList)
  printScore(scoreList, classSum, classAvg)

main()
