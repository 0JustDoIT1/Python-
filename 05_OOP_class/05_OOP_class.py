# 클래스 초기화
# 이등변 삼각형의 넓이
width = 108
height = 20
area = width * height / 2
print("삼각형의 넓이는", area)

def calctri(width, height):
  """이등변삼각형의 넓이를 구하는 함수""" # doc string
  area = width * height / 2
  return area
print("삼각형의 넓이는 ", calctri(width, height))

# 클래스는 데이터 타입으로는 사용자 정의 데이터 타입
# 자료구조적 입장에서 보면 이질적 데이터를 담고 있는 block
# 클래스는 자료구조와 알고리즘으로 구성된 객체다

# class template(틀, 모양)를 선언
# 코드 영역에서 생성 - 미실행상태
class Triangle:
  # 멤버함수는 반드시 첫 번째 매개변수가 self여야 함
  def setData(self, width, height):
    name = " " # 지역변수
    self.width = width # 멤버변수 / 클래스와 수명이 같음
    self.height = height
  def area(self):
    self.position = "대전" # 멤버변수
    return self.width*self.height/2

# 인스턴스 변수
tri1 = Triangle() # 인스턴스 : heap에 멤버변수 영역을 확보하라
tri1.setData(10,20) # 초기화
# 기본이 [public]이기 때문에 직접 접근이 가능
print(tri1.width, tri1.height, tri1.area())

# C 나 JAVA에서는 생성자에서 반드시 초기화
# Python은 어떤 함수에서도 가능 (보통 __init__)
# C 나 JAVA에서는 멤버변수는 구성요소로 설계됨
# Python은 어떤 함수에서도 self를 붙여주면 멤버변수가 됨
# C 나 JAVA는 한번 클래스가 선언이 되면 변경이 불가
# Python은 실시간으로 추가/삭제 가능

# 기본적으로 Python의 접근 지정자는 public
# 데이터를 보호하기 위해서 getter, setter 사용
# 변수에 속성을 주는 것 : property
class C:
  def __init__(self): # 생성자
    self._x = None # 멤버변수
  def getx(self): # getter
    return self._x
  def setx(self, value): # setter
    if value > 120:
      value = 120
    self._x = value
  def delx(self): # deleter
    del self._x # 메모리 해제함수
  x = property(getx, setx, delx, "I'm the 'x' property.")

test = C()
test.x = 100 # 속성을 사용하면 간접 접근
print(test.x)

# 파이썬의 모든 클래스는 object를 상속
class MyClass(object):
  """ 클래스의 예 : 클래스변수, 멤버변수, 지역변수 """
  i = 12345 # 클래스 변수, 공유변수, 정의한 코드를 실행할 때 딱 한번 생
  def __init__(self): # overriding
    self.i = 54321 # 멤버변수
    num = 100 # 지역변수
  def f(self):
    return self.i
  # def printi(self): i는 멤버변수도 아니고 클래스 변수도 아님
  #   print(i)
print(MyClass.__doc__)
print(MyClass.i) # 클래스 변수 호출
myclass = MyClass() # 클래스 인스턴스 : 메모리 확보
print(myclass.i) # 인스턴스 변수는 멤버변수를 가리킴
myclass.f()

# 1970.1.1을 기준으로 지나온 초단위 시간
# ctime 문자 시간
from time import time, ctime, sleep
class Life:
  def __init__(self): # 생성자
    self.birth=ctime() # 문자시간
    print("생성", self.birth)
  def __del__(self): # 소멸자 - 객체가 메모리에서 해제될 때 동작
    print("사망", ctime())
  def test(self):
    print("3초 동안 sleeping")
    sleep(3) # 초
li = Life() # self.birth 메모리 확보
li.test()
del li # 강제로 메모리 해제 - 주소값이 삭제
# Life() 를 참조하던 인스턴스 변수가 삭제되고 참조 카운트가 0
print(time())

class Employee:
  empCount = 0 # 클래스 변수(), 사원 수
  # 생성자는 강제 호출이 불가능
  def __init__(self, name, salary): # 생성자 : 인스턴스 시 자동호출
    self.name = name
    self.salary = salary
    Employee.empCount += 1
  def displayCount(self):
    print("직원 수 = %d" % Employee.empCount)
  def displayEmployee(self):
    print("이름 : ", self.name, ", 급여 : ", self.salary)
  # 파이썬의 클래스는 함수처럼 사용이 가능
  def __call__(self, *pargs, **kwargs): # 오버라이딩
    print("Called:", pargs, kwargs)
# 코드 영역에 저장

emp = Employee("이순신", 500) # 인스턴스 => 메모리 공간확보
emp.displayCount()
emp1 = Employee("강감찬", 500)
emp1.displayCount()
emp.displayCount()

print(f"직원 수는 {Employee.empCount}")
# 인스턴스 변수
emp("빅데타", 500,100, c=100) # __call__ 호출
print(emp1.displayCount())

print(dir(emp))
# class는 dict 형변수를 이용해서 멤버변수를 관리
print(emp.__dict__)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__bases__:", Employee.__bases__)

emp1.age = 7 # 실시간으로 변수 추가 가능
# print(emp.age) 에러 발생 - 인스턴스 변수 해당 변수에만 데이터가 추가

# 속성 CRUD
print(hasattr(emp1, 'name')) # 확인
setattr(emp1, 'age', 8) # 수정
print(getattr(emp1, 'age')) # read / emp1.age
print(hasattr(emp1, 'age'))
delattr(emp1, 'age') # delete 멤버변수 해제도 가능
hasattr(emp1, 'age')

class C:
  def __inaccessible(self): # __붙이면 => private 함수/변수
    print("public을 이용해서 접근했음")
  def accessible(self):
    print("접근 가능")
    self.__inaccessible()
# C().__inaccessible()
C().accessible()

class Student:
  """학생관리"""
  def __init__(self, name, age): # 초기화
    self.name = name
    self.age = age
  def print(self):
    print("이름: ", self.name, " 나이:", self.age)
  # 오버라이딩 __str__
  # __repr__ 숫자를 출력할 때 더 정밀함
  # 문자열을 요구하는 함수의 매개변수로 전달이 되면 텍스트를 리턴
  def __repr__(self):
    return "나의 이름: " + self.name + " 나이: " + str(self.age ) + "입니다."
f = Student("다함께", 23)
f.print()
print(f) # 문자열을 요구하는 함수의 매개변수 : 클래스
print(f.__doc__)
print(f.__class__)
print(f.__dict__)
# 정의 클래스를 이용해서 인스턴스가 가능
g = f.__class__("발전해", 34)
print(g)

# 얕은 복사와 깊은 복사
# 대입 - 주소에 의해 전달
# call by reference
import copy
a=[1,2,3]
b=[4,5,a]
x=[a,b,100]
y=copy.copy(x) # 얕은 복사 - 주소에 의한 복사
t=copy.deepcopy(x) # 깊은 복사 - 값을 복사
e=copy.deepcopy(y)
print("a=",a)
print("x=",x)
print("y=",y) # [a, b, 100] # 주소를 가리킴
print("t=",t) # 값이 들어와 있는 상태
print("e=",e)
####
a.append(100)
print("x=",x) # 주소로 복사했기 때문에 원본을 변경하면 데이터도 변경
print("y=",y)
print("t=",t) # 깊은 복사는 주소 복사가 아니라 값을 복사

print("e=",e)

import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

# 클래스 설계 규칙
# 단일 책임의 원칙 (SRP single resposibility principle)
# 클래스는 하나의 기능을 구현해야 함
import random
class LottoBall:
  def __init__(self, num):
    self.num = num
  def __repr__(self):
    return str(self.num)

class LottoMachine:
  def __init__(self):
    self.ballList = []
    for i in range(1,46):
      self.ballList.append(LottoBall(i))
  def selectBalls(self):
    random.shuffle(self.ballList);
    return self.ballList[0:6]

class LottoUI:
  def __init__(self):
    self.machine = LottoMachine()
  def playLotto(self):
    input("로또를 뽑을까요?");
    selectedBalls = self.machine.selectBalls()
    for ball in selectedBalls:
      print(ball, end=" ")

lo = LottoUI()
lo.playLotto()

# chaining
# 이 클래스는 초기화를 해도 값이 세팅이 안된 상태
# self는 내부적으로 class 주소를 가지고 있음
# self는 인스턴스 될 때 결정
class Person:
  def name(self, value):
    self.name = value
    return self # self를 리턴
  def age(self, value):
    self.age = value
    return self
  def introduce(self):
    print("이름 : ", self.name, ", 나이 : ", self.age)
person = Person()
person.name("에이콘").age(21).introduce() # chaining

# 정적 함수
# self가 있는 메소드는 인스턴스 후에 사용 가능
# 정적 함수는 인스턴스 하지 않고 바로 사용 가능
class StaticTest():
  def __init__(self):
    self.num = 100
  # 정적 함수 방법 1
  def spam(x,y): # self가 없음 -> 일반 함수
    print("일반함수", x, y)
  spam = staticmethod(spam) # 정적 메소드
  # 정적 함수 방법 2
  @staticmethod # decorator 데코레이터
  def spam1(x,y):
    print("정적함수", x, y)
# 대표적인 static 함수 : math 라이브러리
# math().sqrt() => math.sqrt()
StaticTest.spam(1,2) # 인스턴스 없이 사용하는 함수
StaticTest.spam1(1,2)
d=StaticTest() # 인스턴스하고도 접근이 가능
d.spam(1,2)

# class method
# Python은 오버로딩이 기본적으로 안됨
from datetime import date
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # 출생연도 - 생성방법을 변경할 때
  @classmethod
  def fromBirthYear(cls, name, birthYear): # cls는 클래스
    return cls(name, date.today().year - birthYear) # 생성자 다시 호출
  def display(self):
    print(self.name + "의 나이는 : " + str(self.age))
person = Person("강감찬", 19)
person.display()
person1 = Person.fromBirthYear("을지문덕", 1985)
person1.display()

# diagnosis 진단
# 자료구조로서의 class
class Patient:
  def __init__(self, name, age, diagnosis):
    self.name = name
    self.age = age
    self.diagnosis = diagnosis
# 리스트에 저장된 class
# class 인스턴스
patients = [Patient("김철수", 70, "고혈압"), Patient("이영희", 65, "당뇨병"), Patient("박민수", 80, "심부전")]


# 거리값을 구하기 위해
# Point class를 작성하시오
# 멤버변수 : x,y좌표
# 메소드는 __repr__ 출력 오버라이딩
# dist 함수 구현 (거리값을 구하는 함수)
# Collision 함수 구현 (점들이 충돌하는지 체크, 3보다 작으면 충돌)

import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def dist(self, x2, y2):
    distance = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
    return distance

  def collision(self, x2, y2):
    collCheck = self.dist(x2, y2) < 3
    return collCheck

  def collisionUI(self, x2, y2):
    if self.collision(x2, y2):
      print("충돌했습니다.")
    else:
      print("충돌하지 않았습니다.")

  def __repr__(self):
    return f"x좌표: {self.x}, y좌표: {self.y}"

point1 = Point(7,3)
point2 = Point(4,7)
print(point1)
print(point2)
print("두 점 사이의 거리는 ", point1.dist(point2.x, point2.y))
point1.collisionUI(point2.x, point2.y)

# Point class를 이용해서 원(Circle) 클래스를 작성하시오
# 원 : 중심점 + 반지름
# pi : 3.141592
# math.pi
# 원의 둘레를 구하는 함수를 작성하시오 : 2 * pi * r
# 원의 면적을 구하는 함수를 작성하시오 : pi * r**2
# 두 원의 충돌 여부를 판단하는 함수를 작성하시오 (중심점의 거리가 반지름의 합보다 작으면 충돌)
# 중심과 반지름을 출력하는 함수를 작성하시오

# math 라이브러리 추가
import math

# class 생성
class Point:
  # 원주율(파이) 값 class 변수로 선언
  pi = math.pi

  # 생성자
  # 중심점(list 형태), 반지름
  def __init__(self, node, radius):
    self.node = node
    self.x = self.node[0] # 꺼내쓰기 편하려고 세팅
    self.y = self.node[1]
    self.radius = radius

  # 원의 둘레 계산 함수
  def calcCircumference(self):
    # 2 * pi * 반지름
    circumference = 2 * Point.pi * self.radius
    return circumference

  # 원의 면적 계산 함수
  def calcArea(self):
    # pi * 반지름**2
    area = Point.pi * (self.radius ** 2)
    return area

  # 다른 원과의 중심점 거리 계산 함수
  def dist(self, other):
    # 좌표 간의 거리
    distance = math.sqrt((other.node[0] - self.x)**2 + (other.node[1] - self.y)**2)
    print(f"두 점 사이의 거리는 {distance}")
    return distance

  # 충돌 여부 확인
  # 다른 원의 데이터 필요
  # 두 원의 중심점 사이 거리 < 두 원의 반지름 합 = 충돌
  def checkCollision(self, other):
    sumRadius = self.radius + other.radius # 두 원의 반지름 합
    distance = self.dist(other) # 두 원의 중심점 사이 거리
    collision = distance < sumRadius # 충돌 여부 판단
    return collision

  # 충돌 여부 확인 후 메세지 표출
  def checkCollisionUI(self, other):
    if self.checkCollision(other):
      print("충돌했습니다.")
    else:
      print("충돌하지 않았습니다.")

  # print() 함수로 출력하기 위한 __repr__ 오버라이딩
  # 객체를 표현하는 문자열 반환 기능
  def __repr__(self):
    return f"중심점 좌표: {self.node}, 반지름 길이: {self.radius}"


first = Point((0,0), 3)
second = Point((2,3), 6)
print(first)
print(second)
print("원 둘레: ", first.calcCircumference())
print("원 면적: ", first.calcArea())
first.checkCollisionUI(second)