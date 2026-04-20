class Parent(): # 일반클래스 (묵시적으로 Object를 상속)
  def myMethod(self):
    print("부모메소드")
class Child(Parent): # 상속
  def myMethod(self): # 재정의 overriding
    print("자식메소드")
ch = Child()
ch.myMethod()

# 파이썬의 모든 변수는 객체
print(isinstance(1, object))
print(isinstance(Parent, object))
print(isinstance(Child, Parent))
print(isinstance(ch, Parent))
print(isinstance(ch, Child))
print(issubclass(Child, Parent)) # super class / subclass


# 부모 -> 자식, 상태와 행동을 상속
# 상속에서는 상태는 상속받지 않음 : 관례상
class Parent:
  parentAttr = 100 # class 변수
  def __init__(self, name): # 생성자는 상속 받지 않음
    self.name = name
    print("부모 생성자")
  def parentMethod(self):
    print("부모 메소드", self.name)
  def setAttr(self, attr):
    Parent.parentAttr = attr
  def getAttr(self):
    print("부모 속성 : ", Parent.parentAttr)
class Child(Parent):
  def __init__(self): # 자식 생성자, 인스턴스 될 때 자동 호출
    # 상속에서의 예외사항
    # Parent.__init__(self, "대한") # 부모의 생성자 호출
    super().__init__("대한")
    print("자식 생성자")
  def childMethod(self): # 자식에서 추가된 함수
    print("자식 메소드")
  def print_attribute(self): # 추가함수
    self.setAttr(500)
    print("자식호출된 부모 속성 : ", Parent.parentAttr)

# 부모는 자식을 가리킬 수 있음
# 즉, 부모 타입 변수에 자식 객체 할당 가능
c = Child()
c.childMethod()
c.parentMethod() # 상속받았으므로 가능
c.setAttr(200) # class 변수의 값이 변경
print(c.getAttr())
c.print_attribute()
c.parentAttr
papa = Parent("만세")
papa = Child()
papa.childMethod() # C, Java에서는 호출이 안됨
papa.parentMethod()

# duck typing => 상속관계가 아니더라도 대입이 가능
# 굳이 상속을 사용하지 않더라도 대입이 가능
# 그런데 왜 상속을 사용하는가
# 코드 추천을 하는 visual studio code 같은데서 타이핑을 원활하게 추천가능
# 프로그래머의 의도를 파악하지 못하는 경우가 발생함

import math

# 부모의 멤버변수, 자식의 멤버가 분리된 경우
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def translate(self, dx, dy): # 증가
    self.x += dx
    self.y += dy
class Point3D(Point):
  def __init__(self, x, y, z):
    Point.__init__(self, x, y) # x, y만 초기화
    self.z = z
  def translate(self, dx, dy, dz):
    Point.translate(self, dx, dy)
    self.z += dz

class Shape:
  def __init__(self):
    print("부모 클래스 ")
  def area(self):
    print("면적")
  def perimeter(self):
    print("둘레")
  def display(self):
    self.area()
    self.perimeter()

# 이등변 삼각형
class Triangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def area(self):
    print("삼각형의 넓이는 = ", self.width * self.height / 2)
  def perimeter(self): # 대각선의 길이는 2개
    print("삼각형의 둘레는 = ", self.width + math.sqrt(math.pow(self.width / 2, 2) + math.pow(self.height, 2)) * 2)

# 문제
# 사각형 (Rectangle class를 상속 구현하시오)
# 둘레 : 밑변*2 + 높이*2
# 면적 : 밑변*높이
# Shape를 상속받아서 구현, point를 멤버변수로

class Rectangle(Shape):
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2
    self.width = self.point1.x - self.point2.x
    self.height = self.point1.y - self.point2.y

  def area(self):
    print("사각형의 넓이는 = ", abs(self.width) * abs(self.height))

  def perimeter(self):
    print("사각형의 둘레는 = ", (abs(self.width) + abs(self.height)) * 2)

A = Rectangle(Point(0,1), Point(2,4))
A.display()

# 원 (Circle class)를 구현하시오
# point, radius를 멤버 변수로
# 둘레 : 2 * math.pi * radius
# 면적 : math.pi * radius**2

class Circle(Shape):
  def __init__(self, point, radius):
    self.point = point
    self.radius = radius

  def area(self):
    print("원의 넓이는 = ", math.pi * self.radius**2)

  def perimeter(self):
    print("원의 둘레는 = ", 2 * math.pi * self.radius)

B = Circle([1,2], 3)
B.display()

import random

shape_list=[]
for i in range(500):
  rand = random.randint(0, 10)
  if rand%3 == 0:
    width = random.randint(1,10)
    height = random.randint(1,10)
    tri = Triangle(width, height)
    shape_list.append(tri)
  elif rand%3 == 1:
    x = random.randint(1,10)
    y = random.randint(1,10)
    rect = Rectangle(Point(10,20), Point(x,y))
    shape_list.append(rect)
  else:
    r = random.randint(1,10)
    ci = Circle(Point(10,20), r)
    shape_list.append(ci)

# 객체지향프로그래밍 설계 원칙
# 1. 단일 책임의 원칙
# 2. 리스코프의 원칙(LSP: Liskov Substitution Principle)
#   리스코프의 원칙 (자식은 부모를 완전히 대체할 수 있어야 함)
# 3. 인터페이스 분리의 원칙 (출력, 작업 - 사용하지 않는 것에 의존하면 안됨)

# 상속할 때 가능한 한 자식 메소드는 최소화하는게 좋음
for i in range(5):
  shape_list[i].display()

# 평가 방법과 인터페이스 분리
class Evaluation:
  def printcalcGrade(self, average):
    pass # None 객체
class Hakjum(Evaluation):
  def printcalcGrade(self, average):
    if average >= 90:
      return "A"
    elif average >= 80:
      return "B"
    elif average >= 70:
      return "C"
    elif average >= 60:
      return "D"
    else:
      return "F"
class Evaluation_print:
  # 매개변수가 부모
  def print_evaluation(self, evaluation): # 의존성 주입(Dependency Injection)
    jumsu = int(input("점수를 입력하시오: "))
    print(evaluation.printcalcGrade(jumsu))

ha = Hakjum()
ev = Evaluation_print()
ev.print_evaluation(ha)

# 평가 방법 변경 -> 합격 불합격
class Pass_Fail(Evaluation):
  def printcalcGrade(self, average):
    if average >= 60:
      return "합격"
    else:
      return "불합격"
class Element_Evaluation(Evaluation):
  def printcalcGrade(self, average):
    if average >= 90:
      return "수"
    elif average >= 80:
      return "우"
    elif average >= 70:
      return "미"
    elif average >= 60:
      return "양"
    else:
      return "가"
pass_fail = Pass_Fail()
element = Element_Evaluation()
# 인터페이스 수정없이 평가 방법만 수정해서 유지하는 것이 가능
ev.print_evaluation(pass_fail)
ev.print_evaluation(element)

evaluation_method = []
evaluation_method.append(ha)
evaluation_method.append(pass_fail)
evaluation_method.append(element)

for evalu in evaluation_method:
  ev.print_evaluation(evalu)

# 문제
# 학생 1명의 정보를 저장하는 Student class를 작성하시오
# 이름, 국어, 영어, 수학, 합계, 평균, 학점
# 합계와 평균을 구하는 함수
# 학점을 구하는 함수
# 데이터를 입력받는 함수
# 출력 함수

class Student:
  def __init__(self, name='', kor=0, eng=0, math=0, total=0, average=0, grade=''):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = total
    self.average = average
    self.grade = grade

  def calcTotal(self):
    return self.kor + self.eng + self.math

  def calcAverage(self):
    return round(self.calcTotal() / 3, 2)

  def calcGrade(self, point):
    if point >= 90:
      return "A"
    elif point >= 80:
      return "B"
    elif point >= 70:
      return "C"
    elif point >= 60:
      return "D"
    else:
      return "F"

  def getStudentData(self):
    self.name = input("이름을 입력하시오: ")
    self.kor = int(input("국어: "))
    self.eng = int(input("영어: "))
    self.math = int(input("수학: "))
    self.total = self.calcTotal()
    self.average = self.calcAverage()
    self.grade = self.calcGrade(self.average)

  def __repr__(self):
    return "%5s %6.2f %6.2f %6.2f %6.2f %6.2f %5s" % (self.name, self.kor, self.eng, self.math, self.total, self.average, self.grade)

  # def __repr__(self):
  #   return f"{self.name:5} {self.kor:6.2f} {self.eng:6.2f} {self.math:6.2f} {self.total:6.2f} {self.average:6.2f} {self.grade:5}"

A = Student()
# A.getStudentData()
print(A)

# diamond 문제
class A:
  def m(self):
    print("A.m()호출")

class B(A):
  def m(self):
    print("B.m()호출")

class C(A):
  def m(self):
    print("C.m()호출")

class D(B,C): # 구현이 되었다면 최우선은 D
  pass

dinc = D()
dinc.m() # 어떤 메소드가 실행이 되는가
print(D.__mro__) # method resolution order

# duck typing
# 파이썬은 완전 객체 지향 언어
# 상속: 부모는 자식을 가리킬 수 있음
#   C++, Java 데이터 지향 스타일언어 (반드시 타입 지정)
# 그렇더라도 상속 구조 사용해야 함 (IDE: visual studio code)

a=10
a="test"
class Guard: # 상속 무
  def three_point(self):
    print("가드는 3점슛 장착")
  def apass(self):
    print("가드의 핵심은 에이패스지")
class Jordan: # 일반클래스 상속 무
  def three_point(self):
    print("조단은 3점슛 장착")
  def apass(self):
    print("조단은 에이패스 가능")

def inhecourt(duck): # 부모 매개변수가 아님 (Dependency Injection이 아님)
  duck.three_point()
  duck.apass()

gu = Guard()
gu.three_point()
gu.apass()
jo = Jordan()
jo.three_point()
jo.apass()
inhecourt(gu)
inhecourt(jo)

class Clock(object):
  def __init__(self, hours=0, minutes=0, seconds=0):
    self.__hours = hours
    self.__minutes = minutes
    self.__seconds = seconds

  def set(self, hours, minutes, seconds=0):
    self.__hours = hours
    self.__minutes = minutes
    self.__seconds = seconds

  def tick(self):
    # 초가 만땅
    # 초침, 분침, 시침 == 0
    if self.__seconds == 59:
      self.__seconds = 0
      if (self.__minutes == 59):
        self.__minutes = 0
        if (self.__hours == 23):
          self.__hours = 0
        else:
          self.__hours += 1
      else:
        self.__minutes += 1
    else:
      self.__seconds += 1

  def check(self):
    if self.__hours == 0 and self.__minutes == 0 and self.__seconds == 0:
      return True

  def display(self):
    print("%d:%d:%d" % (self.__hours, self.__minutes, self.__seconds))

  def __str__(self):
    return "%2d:%2d:%2d" % (self.__hours, self.__minutes, self.__seconds)


x = Clock()
x.set(10, 30, 50)
print(x)
x.display()

# 문제
# tick을 이용해서 17시 50분을 만들어 보시오
y = Clock(12,16,0)
for i in range((5*60*60)+(34*60)):
  y.tick()
print(y)

# 달력
class Calendar(object):
  months = (31,28,31,30,31,30,31,31,30,31,30,31)
  def __init__(self, day=1, month=1, year=1900):
    self.__day = day
    self.__month = month
    self.__year = year

  def leapyear(self, y):
    if y % 4: # 4로 나누어서 떨어지지 않으면 윤년이 아님
      return 0
    else: # 윤년
      if y % 100: # 100으로 나누어서 떨어지지 않으면 윤년
        return 1
      else:
        if y % 400:
          return 0
        else:
          return 1

  def set(self, day, month, year):
    self.__day = day
    self.__month = month
    self.__year = year

  def advance(self):
    months = Calendar.months
    max_days = months[self.__month - 1]

    if self.__month == 2:
      max_days += self.leapyear(self.__year)
    if self.__day == max_days:
      self.__day = 1
      if(self.__month == 12):
        self.__month = 1
        self.__year += 1
      else:
        self.__month += 1
    else:
      self.__day += 1

  def __str__(self):
    return str(self.__year) + "/" + str(self.__month) + "/" + str(self.__day)

# 문제
# 달력을 오늘 날짜로 표현하시오
today = Calendar()
for i in range(((2026 - 1900)*365) + (30*4) + 2):
  today.advance()
print(today)

# 문제
# Clock class + Calendar class를 다중 상속받아서
# 시간이 가면 날짜도 진행되도록 두개를 연결 구현해 보시오
# - 시분초가 모두 0일 때 -> 날짜 하나 증가

class ClockCalendar(Clock, Calendar):
  def __init__(self, hours=0, minutes=0, seconds=0, day=1, month=1, year=1900):
    Clock.__init__(self, hours, minutes, seconds)
    Calendar.__init__(self, day, month, year)

  def __str__(self):
    return Calendar.__str__(self) + ", " + Clock.__str__(self)

  def tick_advance(self):
    self.tick()
    if self.check():
      self.advance()

x = ClockCalendar(23,59,58,1,1,2020)
for i in range(2):
  x.tick_advance()

print(x)

# 주말 문제

# 1인분의 성적을 저장할 수 있는 클래스를 작성하시오 (기본 클래스)
# 리스트에 CRUD하는 manager class를 작성하시오
# menu를 작성해서 CRUD를 관리하는 main class를 작성하시오

# while문: 1.입력 2.출력 3.수정 4.삭제 5.정렬 6.등수 9.종료

