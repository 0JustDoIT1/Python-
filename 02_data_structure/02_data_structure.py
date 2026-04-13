# []:list, indexing
# {}: dict, set
# (): tuple, 함수
a = [1, 2, 3, 4, 5] # 리스트 초기화
b = a[0:2] # slicing
print(b)
print(type(b)) # slicing한 결과도 list

a = [1, 2, 3]
# stack -> [주소, 주소, 주소]
# heap -> 1, 2, 3
# casting 형변환
# int("23")
b = str(a[2]) + " hi" # concatenation 문자열 결합
print(b)

# 파이썬의 list의 특징
# 동적 배열 (c의 배열 + linked list(메모리 비효율적 - 앞뒤에 주소를 달아야 해서))
# 이질적 데이터를 저장
# 공간 size 변화가 가능하다 12% 자동증가
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

# 3차원 list
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[0])
print(a[2][2][0])
len(a)
len(a[2])

# 리스트 수정
a = [1, 2, 3]
a[2] = 4
print(a)
# 범위가 있으면 그 범위를 대체하고
a[1:2] = ['a', 'b', 'c'] # 풀어져서 입력
print(a)
# 하나의 인덱스 인 경우는 모양을 유지하면서 입력
a[2] = ['하나', '둘', '셋']
print(a)
# 2차원 배열 생성
# 사이즈가 다르면 for 사용에 제약
mat = [[1,2,3], [4,5,6],[7,8,9]]
print(mat)

a = [1,2,3,4,5]
b = range(1,6,1)  # 일반 for문과 같음
print(b)
# python의 반복문은 for in 문
for i in a:
    print(i)
for i in b:
    print(i)
list(b)
c = range(1,6,2)
list(c)

b = range(0,5,1)
for i in b:
    print(i)
    print(a[i])

# 리스트 객체
# append : 뒤에 추가
# pop : 뒤에 삭제
a = [10,20,30,40,50]
a.append(60) # [10,20,30,40,50,60]
print(a.pop())
a.append(70) # [10,20,30,40,50,70]
a.append(80) # [10,20,30,40,50,70,80]
print(a.pop()) # [10,20,30,40,50,70]
print(a)
print(a.pop(0)) # [20,30,40,50,70]
print(a)

# true/false
# printer = [] # 리스트 거짓 : 데이터 없음
# printer.pop()

printer = [] # false
if not printer: # 조건식이 참이 되어야 동작
    print("리스트가 비어 있습니다. ")
printer.append(60)
printer.append(50)
if not printer:
    printer.pop()
printer.append(40)
print(printer.pop(0))
printer

# 함수 : 반복되는 코드 중복을 방지하기 위해 정의된 코드
# define
# 함수명(파라미터)
# 파이썬은 데이터 타입을 지정하지 않음 - 변수는 다 포인터이기 때문에
# 주소값을 담고 있어서 타입을 필요로 하지 않음
# 타입을 확인하는 책임은 프로그래머에게 있음
# 함수의 개변수는 반드시 개수가 일치해야 됨
# 호출한 곳으로 돌아가기 위해서 return
# 데이터 타입을 지정하지 않는 편리함 대신에 데이터 타입을 확인해서 함수를 사용해야 함
def calc(a,b): # block
  return a+b, a*b # 들여쓰기 - 멀티 리턴 가능 (파이썬의 특징)
x,y = calc(3,4)
print(x,y)
print(x)
x,y
args=(4,5) # 데이터 타입 tuple - 수정 불가 - 속도가 빠름
calc(*args) # * 풀어씀

# {} dict, set
d = {'one':1, 'two':2}
print(d.items())
print(d.keys()) # key들의 집합
print(d.values()) # value들의 집합

# () tuple
cities = ('seoul', 'incheon', 'suwon')
print(cities.index('suwon'))
print('incheon' in cities) # 포함 연산자
print(cities.count('seoul'))
print(sorted(cities)) # 오름차순(사전순) 정렬
sorted(cities, reverse =True) # 내림차순

# CRUD (create, read, update, delete)
# 생성 : []
# 읽기 : index
# 수정 : append, extend, 인덱스대입
# 삭제 : remove, pop
cities = ['seoul', 'incheon','suwon']
print(cities)
cities.append('busan')
print(cities)
cities.insert(0, 'daegu') # 인덱스 삽입
print(cities)
other_cities = ['jeju', 'kwangju']
print('결합', cities + other_cities) # 결합
# append 모양을 유지하면서 추가
cities.append(['daejeon', 'ulsan'])
# extend 풀어져서 추가
cities.extend(['jeju', 'kwangju'])
print(cities)
cities.extend(['jeju', 'kwangju'])
print(cities)
print(cities.index('seoul')) # 인덱스 확인
print('daegu' in cities) # 포함연산자
cities.append(['daegu', 'ulsan'])
print(cities)
print(cities[0])
print(cities[10][0])
cities.remove(cities[10]) # 데이터를 이용해서 삭제
print(cities)

print(bin(3)) # 2진수
print(hex(255)) # 16진수 (2진수에서 4자리)
print(oct(15)) # 8진수 (2진수에서 3자리)

# enumerate : 인덱스와 데이터가 필요한 경우 사용
seasons = ['Spring', 'Summer', "Fall", "Winter"]
# range 객체의 내부 확인 : list casting
print(enumerate(seasons)) # enumerater 객체
print(list(enumerate(seasons)))
# 인덱스 시작번호 수정
print(list(enumerate(seasons, start = 1)))
print(seasons[1])

# 정렬(sort) -> 검색을 빠르게 하기 위함
# hash 함수에 의한 검색
# list에서 빠른 검색은 이진검색 -> 정렬
listexam = [("대한", 1), ("민국", 3), ("만세", 6), ("야호", 1)]
# list의 정렬함수(1번째 요소를 기준, 오름차순)
listexam.sort()
print(listexam)
# 두번째 요소로 정렬하고 싶은 경우
# 람다함수(무명함수 - 이름이 없음)
# 반복해서 사용하지 않고 한번 쓰고 버림
# def fun(row):
#     return row[1]
listexam.sort(key=lambda row: row[1])
print(listexam)
listexam.sort(key=lambda row: row[1], reverse=True)
print(listexam)

# 만세를 대군으로 수정하시오
listexam = [("대한", 1), ("민국", 3), ("만세", 6), ("야호",1)]

# tuple을 list로 변환하고 데이터를 수정
for index, data in enumerate(listexam):
    print(data)
    listexam[index] = list(data)

listexam[2][0]="대군"
listexam

school = []
name = input("이름을 입력하시오: ")
kor = eval(input("국어점수를 입력하시오!"))
school.append([name,kor]) # 모양유지
name=input("이름을 입력하시오: ")
kor = eval(input("국어점수를 입력하시오!"))
school.append([name,kor])
name = input("이름을 입력하시오: ")
kor = eval(input("국어점수를 입력하시오!"))
school.append([name,kor])
# 점수를 기준으로 정렬
school.sort(key=lambda row: row[1], reverse=True)
print(school)
print(list(school))

school = []
# index가 아닌 반복 횟수
for i in range(3):
    name = input("이름을 입력하시오: ")
    kor = eval(input("국어점수를 입력하시오: "))
    pair = []
    pair.append(name)
    pair.append(kor)
    school.append(pair)
school.sort(key=lambda row: row[1], reverse=True)
print(school)

# 문제
# 둔산중학교는 3학년으로 이뤄져 있고
# 한 학년은 2개의 반으로 구성이 되어져 있고
# 학생은 3명이다.
# 이 데이터를 list에 입력하시오

school = []
# 18번을 반복하면서 데이터를 생성
# 중첩 for 문
# 프로그램은 순차적으로 실행
# 순서를 변경하는 것이 제어문
# for, if, while, match 문 exception(예외처리) 문
for i in range(3):
    grade = []
    # grade = input("학년을 입력하시오: ")
    for j in range(2):
        className = []
        # className = input("반을 입력하시오: ")
        for k in range(3):
            name = input("이름을 입력하시오: ")
            kor = eval(input("국어점수를 입력하시오: "))
            pair = []
            pair.append(name)
            pair.append(kor)
            className.append(pair)
        grade.append(className)
    school.append(grade)

print(school)

sungjuk=[['하하', 100,100,100], ['유재석', 99,99,98], ['추신수', 90,98,91]]
# 문제
# 1) 합계를 내서 4번째 인덱스에 입력
# 2) 합계를 3으로 나누어서 평균을 구해 5번째 입력하시오(소수점 2번째 자리에서 반올림하시오)
# 3) 합계를 기준으로 내림차순으로 정렬하시오
# 4) 6번째 인덱스에 등수를 입력하시오
# 5) 출력하시오

for i in sungjuk:
    sum = i[1]+i[2]+i[3]
    # avg = int(sum / 3 * 100) / 100
    avg = round(sum/3, 2)
    i.append(sum)
    i.append(avg)

sungjuk.sort(key=lambda row: row[4], reverse=True)

for i in sungjuk:
    i.append(sungjuk.index(i)+1)

print(sungjuk)

for i in range(len(sungjuk)):
    for j in range(len(sungjuk[i])):
        print(sungjuk[i][j], end=" ")
    print() # enter 효과

# 추가 문제 : 이름을 기준으로 다시 정렬해서 출력하시오
sungjuk.sort(key=lambda row:row[0])
print(sungjuk)


# 2의 10승을 계산하시오
2**10 # 단항연산자

i = 10
i = ++i # 전위 단항연산자
i

# 증가 변수
# 누적 변수
i = 1 # 초기화
i = i+1 # 증가변수
hab = 0
hab = hab + i # 누적변수
print(hab)

num1 = 6
num1 += 1 # 속도가 더 빠름
num2 = 7
num2 -= 5
num3 = 8
num3 /= 2
# 수학함수
# 소수점 n+1 자리에서 반올림하여 n자리까지 표현
print(num1, num2, round(num3, 2))
num1 = 1
num1 *= 3
num2 = 2
num2 **= 3
print(num1, num2)

a = 2
b = 3
# 연산자 우선순위
print(abs(1 - (4 * b))) # 절대값
print(int((a ** b) + .8))
print(a / b)
print(round(a / b, 3))

a = 9
b = 4
print(add := a + b) # 코끼리 연산자 : 대입과 동시에 값을 리턴
sub = a - b
mul = a * b
div1 = a / b
div2 = a // b # 몫 연산자
mod = a % b # 나머지 연산자 == 경우의 수
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)

# 관계연산자 => True / False
a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# 논리연산자 (and, or, not)
# or => 앞의 변수 값이 참이면 뒤의 변수는 처리하지 않음
a = True
b = False
print(a and b)
print(a or b)
print(not a)

# 비트연산자
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b) # xor 다르면 참
print(a >> 2)
print(a << 2)

# dict에서도 hash를 사용
# 가능한 중복이 없게 개발됨 - 메모리는 한정적이기 때문에 중복이 발생할 수 있음
person = {
    "name": "대한이",
    "age": 30,
    "skills": ["Python", "AI"]
}

print(person["name"]) # 키 값을 참조
person["age"] = 31
person["city"] = "Seoul" # 없으면 추가 / 있으면 수정
print(person)
print("city" in person)
# print(person["sky"]) # 없는 키를 찾으면 에러 발생
person.get("sky", -1)

import hashlib
a = "대한민국"
print(hash(a))
print(id(a))

# 가급적 중복되지 않고 고정 길이로 출력 => 암호화
# 불가역성
# 암호화 값을 DB저장

# 함수도 dict의 value로 가능
# dict도 객체
foo = {
    'bar': 1,
    'foobar': 2,
    'method': lambda x: x**2 # value가 함수
}
foo['method'](2) # key로 호출
# 파이썬의 최상위 오브젝트 객체인 object를 상속받아서 자동으로 호출가능
# 상속받는 이유 : 코드 중복 방지
print(foo.__class__) # 멤버변수 -> dict
print(foo.keys())
print(foo['method'](2))