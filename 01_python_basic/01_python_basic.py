# 데이터를 처리하려면 메모리에 로딩
# 변수는 메모리의 주소값을 의미함
a = 10 # 대입연산자
b = a
print(a)
print(b)
# 변수가 가지고 있는 주소값을 확인하는 함수가 id
print("주소값 대입", id(a)), print(id(b))
a = 20
print(a)
print(b)
print("주소값대입", id(a)), print(id(b)) # 주소가 서로 상이

# 데이터를 해석하려면 데이터 타입이 필요
# 파이썬은 자동으로 데이터를 해석해서 입력
a=10 # 10은 heap에 저장, a에는 heap의 주소
# a="문자를 입력"
# 컴퓨터는 함수베이스로 동작 (function)
# 데이터를 메모리에 저장하고 함수가 데이터 처리
# 객체지향프로그래밍에서 멤버변수 + 메쏘드(method) 하나의 데이터타입 => class
# 간편해진다 => 프로그램의 발전은 프로그래머의 편리성을 발전
print(type(a)) # <class 'int'>
# 파이썬은 모두가 객체다, 파이썬의 변수는 포인터 변수(주소값을 저장)
a.bit_length() # 10을 2진수로 표현할 때 몇 비트가 필요한가

problem = input("수식을 입력하시오") # 입출력은 text
print(problem)
print(eval(problem)) # 형변환 (수식을 인식한 다음 계산)
type(problem) # string
# 문제 eval로 형변환한 데이터 타입을 확인하시오
# 함수에 함수를 전달함 : 1급 객체 (javascript)
print(type(eval(problem)))

# 파이썬의 데이터 타입은
# int(4바이트 이상을 저장가능), float, (long : int형으로 대체), Decimal
# float 부동소수점수 : 32.123 => 0.32123(가수부) + 10 ^2(지수부)
# 지수부 1바이트 - 가수부 3바이트
# 무한루프, 정확하지 않고 1을 0.999999999999999999999
# Decimal을 이용해서 금액 계산
# double quatation
print(int("23")) # 문자열로 입력해야 정확해짐
print(float("23"))
print(eval("23"))
print(eval("23.5"))
x = 5
print(eval("23 + (2 * x)")) # 수식에 있는 변수 이름을 인식
x = 5.0
print(eval("23 + (2 * x)"))

from decimal import Decimal
price1 = Decimal('100.10')
price2 = Decimal('200.20')
total = price1 + price2
print(total)

a3 = 4.24e-3 # exponent 지수형
a4 = 0o177 # Octal 8진수(0~7까지로 제한)
print(a3)
print(a4) # 10진수
# ** : 거듭제곱연산자
# 연산순위 : 단항연산자, 이항연산
print((1*8**2) + (7*8**1) + (7*8**0))
64 + 56 + 7

# 10:a, 11:b, 12:c, 13:d, 14:e, 15:f
a5 = 0x8f # hexa 16진수
print(a5)
print(type(a5))
15 + 8*16**1

# print형식
# % format -> C 방식 (s : string, i : integer)
# format 함수 -> c# 방식
# f-string -> 최근 나온 방식
print('My name is %s and I am from %s , %i .' % ('AI', '4차산업혁명', 10))
# 인덱스가 0부터 시작
print('My name is {1} and I am from {0} and I like {thing}'.format('딥러닝','AI', thing='cats'))
name="김종호"
age=20
print(f"이름은 {name} 나이는 {age}")

# 문자열은 기본적으로 1차원 배열이다. / 사이즈가 다양함
# 파이썬 문자열
# 문자열은 연속된 메모리 공간에 저장
# immutable합니다. (수정이 불가능)
# 인덱스로 접근이 가능
# 모든 파이썬 변수는 객체다 (데이터 + 함수)
# 문자열 개수를 같이 저장
fullName = input("이름을 입력하세요: ") # 문자열로 str
# 공백도 문자
# 인덱스를 리턴
n = fullName.rfind(" ") # reverse find

print(fullName[0])
print(fullName[1])
print(fullName[2])
print(n)
# []는 인덱스에 사용
# () 함수, tuple에 사용
# {} dict형에 사용
print("이름:", fullName[n+1:]) # n: => 끝까지
print("성(s):", fullName[:n]) # :n => 처음부터(뒤에 것은 제외)
print("성(s):", fullName[1:3])

# 문자열을 만드는 3가지 방법
# '', "", """ """ (형태 유지)
""" 건양대
    바이오
"""
t = 'Seoul, Incheon, won'.split(',') # 리스트
print(t) # list
# 문자열 -> 리스트로 출력
print(','.join(t))
type(','.join(t))
# 자료구조 (대량의 데이터를 일정한 형식으로 저장)
# 중요한 조건 : 용량을 줄이거나, 검색 속도를 빠르게 하거나
# [] : 인덱스, list 동적 배열(연속적인 메모리에 저장)
# () : 함수, tuple (list하고 형식이 같은데 수정이 불가능)
# tuple은 함수의 리턴값이나 매개변수로 사용 (속도가 빠름)
# {} : dict, set
# dict(dictionary => key: data 형식) 는 검색 속도가 빠름
# NoSQL는 key: data 형태로 데이터를 저장해서 검색 속도가 빠름