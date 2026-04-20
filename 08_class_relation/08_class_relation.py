# 연관관계
# 멤버변수로 연결

class Teacher:
  def __init__(self, name): # 생성자
    self.name = name  # 멤버변수
  def __repr__(self): # 오버라이딩 : 문자열을 요구하는 함수
    return f"이름:{self.name}"

class Student:
  def __init__(self, name, teacher):
    self.name = name
    self.teacher = teacher  # 클래스 간의 관계는 연관관계
  def __repr__(self):
    return f"학생이름:{self.name}, 선생이름:{self.teacher}"

te = Teacher("김종호")  # 인스턴스
st = Student("박철순", te)
print(st)

# 집합관계(Aggretation) : 두 개의 클래스 간의 관계
# 여러 개의 연관관계의 모음

class Department: # 부서 조직
  def __init__(self):
    self.professors = [] # 리스트 - 자료구조

class Professor:  # 부서 직원
  def __init__(self, name):
    self.name = name

prof1 = Professor("김종호")
prof2 = Professor("박철순")

math_dept = Department()
math_dept.professors.append(prof1)
math_dept.professors.append(prof2)

# 포함관계(Composite)

class House:
  def __init__(self):
    self.room = Room() # 클래스 내부에서 instance
  def __str__(self):
    return self.room.size

class Room:
  def __init__(self):
    self.size = "10평"

ho = House()
print(ho)
del(ho)

# 일반화 관계(상속관계)
# 부모의 이름으로 자식을 대신할 때
# 대신이 가능한 것은 부모의 있는 내용만 가능

class Animal: # super class 부모 클래스
  def speak(self):
    return "동물이 말한다"

class Dog(Animal): # sub class 자식 클래스
  def speak(self):  # 오버라이딩(부모 클래스와 함수 이름이 동일한데 재정의 통해서 다른 행동을 함)
    return "멍멍"
  def __str__(self):  # 자식에 추가된 내용 (리스코프 치환의 원칙)
    return self.speak()

dog = Dog()
print(dog)

# 실현관계(realization)
# abc(abstract base class)

# 추상함수는 반드시 오버라이딩 => 하나의 약속이 됨(plugin)

from abc import ABC, abstractmethod # 추상함수

# 파이썬에서 추상클래스는 ABC 클래스를 상속받아서 구현
class Drawable(ABC):  # 추상클래스
  @abstractmethod # 추상함수
  def draw(self):
    pass

class Circle(Drawable): # 추상클래스 상속
  def draw(self): # 오버라이딩(반드시 오버라이딩 필요)
    print("원을 그립니다")

ci = Circle()
ci.draw()
# dr = Drawable() # 추상클래스는 인스턴스가 안됨

# 요구사항 : UML을 먼저 설계하고 코드로 구현하시오
# School 클래스는 학교 이름(name)과 학생 목록(students)을 가진다.
# Student 클래스는 학생 이름(name)을 가진다.
# 학교는 여러 명의 학생을 등록할 수 있다.
# 학생은 학교 외부에서 독립적으로 생성된다.
# 학교에 등록된 학생들의 이름을 리스트 형태로 출력하시오

class School:
  def __init__(self, name):
    self.name = name
    self.studentList = []

  def addStudent(self, student):
    self.studentList.append(student)

class Student:
  def __init__(self, name):
    self.name = name

school = School("한남대학교")
studentA = Student("허병철")
studentB = Student("테스트")

school.addStudent(studentA)
school.addStudent(studentB)

nameList = [s.name for s in school.studentList]
print(nameList)

class Hospital:
  def __init__(self, name):
    self.name = name
    self.doctors = []

  def add_doctor(self, doctor):
    self.doctors.append(doctor)

class Doctor:
  def __init__(self, name, speciality):
    self.name = name
    self.speciality = speciality

hospital = Hospital("건양대병원")

doctorA = Doctor("허병철", "외과")
doctorB = Doctor("테스트", "내과")

hospital.add_doctor(doctorA)
hospital.add_doctor(doctorB)

print([d.name+"-"+d.speciality for d in hospital.doctors])

# 학생관리 (dict 형을 활용)
class Student:
  def __init__(self, id, name, age, grade):
    self.id = id
    self.name = name
    self.age = age
    self.grade = grade

  def __str__(self):
    return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class Management:
  def __init__(self):
    self.students = {}

  def add_student(self, student): # 학생 추가
    self.students[student.id] = student

  def get_student(self, id):  # 학생 조회
    return self.students.get(id, None)

  def remove_student(self, id): # 학생 삭제
    if id in self.students:
      del self.students[id]

  def display_student(self):  # 학생 출력
    for student in self.students.values():
      print(student)

student1 = Student(1, "대한", 20, "A")
student2 = Student(2, "민국", 21, "B")
manager = Management()
manager.add_student(student1)
manager.add_student(student2)
manager.display_student()
print("\nID 1번 학생: ", manager.get_student(1))
manager.remove_student(1)
manager.display_student()

import sys
class Student:
  def __init__(self, name="", kor=0, mat=0, eng=0, total=0, average=0.0, grade=''):
    self.name = name
    self.kor = kor
    self.mat = mat
    self.eng = eng
    self.total = total
    self.average = average
    self.grade = grade

  def inputData(self):
    self.name = input("이름을 입력하세요")
    self.kor = eval(input("국어 점수: "))
    self.mat = eval(input("수학 점수: "))
    self.eng = eval(input("영어 점수: "))

  def calcSemGrade(self):
    if self.average >= 90:
      return "A"
    elif self.average >= 80:
      return "B"
    elif self.average >= 70:
      return "C"
    elif self.average >= 60:
      return "D"
    else:
      return "F"

  def calc_total_average(self):
    self.total = self.kor + self.mat + self.eng
    self.average = round(self.total / 3, 2)
    self.grade = self.calcSemGrade()

  def __repr__(self):
    return f"{self.bunho:5d} {self.name:5s} {self.kor:6.2f} {self.mat:6.2f} {self.eng:6.2f} {self.total:7.2f} {self.average:7.2f} {self.grade:5s}"

# Facade Design Pattern 를 적용
class Management:
  schoolName = "미래 융합 교육원"
  bunho = 0

  def __init__(self):
    print("메뉴를 선택하시오")
    self.sungjuk=[]

  def add_student(self, student):
    Management.bunho += 1
    student.bunho = Management.bunho
    self.sungjuk.append(student)

  def print_sungjuk(self):
    for per in self.sungjuk:
      print(per)
      print()

  def calc_sungjuk(self): # 재계산하고 싶은 경우
    for per in self.sungjuk:
      per.calc_total_average()

  def search_name(self): # 순차검색
    name = input("검색할 학생 이름을 추가하시오")
    for per in self.sungjuk:
      if(per.name == name):
        print(per)
        return
    print("검색하고자 하는 학생이 없습니다")
    return

  def update_sungjuk(self, name, kor, mat, eng):
    for per in self.sungjuk:
      if(per.name == name):
        per.name = name
        per.kor = kor
        per.mat = mat
        per.eng = eng
        per.calc_total_average() # 자동 계산

  def delete_sungjuk(self, name):
    for per in self.sungjuk:
      if(per.name == name):
        self.sungjuk.remove(per)

sj=["번호", "이름", "국어", "수학", "영어", "총점", "평균", "학점"]
menu=["입력(1), 출력(2), 계산(3), 검색(4), 수정(5), 삭제(6), 종료(9)"]

man_sung = Management()

class Main:
  def __init__(self):
    self.man_sung = Management()

  def run(self):
    while 1:
      sel = input(menu)
      if sel == "1": # 입력
        stu = Student()
        stu.inputData()
        self.man_sung.add_student(stu)
        continue
      elif sel == "2":
        print(Management.schoolName + "    성적 계산표")
        print(f"{"번 호":5s} {"이 름":5s} {"국 어":6s} {"수 학":6s} {"영 어":6s} {"총 점":7s} {"평 균":7s} {"학 점":5s}")
        self.man_sung.print_sungjuk()
        continue
      elif sel == "3":
        self.man_sung.calc_sungjuk()
        print("계산이 완료 되었습니다")
        continue
      elif sel == "4":
        self.man_sung.search_name()
        continue
      elif sel == "5":
        name = input("수정할 이름을 입력하시오")
        kor = input("국어 점수")
        mat = input("수학 점수")
        eng = input("영어 점수")
        self.man_sung.update_sungjuk(name, kor, mat, eng)
        continue
      elif sel == "6":
        name = input("삭제할 이름을 입력하시오")
        self.man_sung.delete_sungjuk(name)
        continue
      elif sel == "9":
        break;
      else:
        print("잘못된 입력입니다. 다시 입력하세요")
        continue

main = Main()
main.run()

# 문제
# - 합격 불합격으로 평가하는 학생과
# - 수우미양가로 평가하는 학생 등 3가지 학생을 동시에 관리하고자 한다
# - 이를 구현하시오
# - 먼저 프로그램 설계를 UML을 이용해서 구현한 다음 코딩하시오

class Student:
  def __init__(self, name="", kor=0, eng=0, math=0, total=0, avg=0.0, grade=""):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = total
    self.avg = avg
    self.grade = grade

  def inputData(self):
    self.name = input("이름을 입력하세요")
    self.kor = eval(input("국어 점수: "))
    self.eng = eval(input("영어 점수: "))
    self.math = eval(input("수학 점수: "))
    self.total = self.kor + self.eng + self.math
    self.avg = round(self.total / 3, 2)

  def calcGrade(self):
    pass

  def __repr__(self):
    return f"{self.name:5s} {self.grade:5s} {self.kor:6.2f} {self.math:6.2f} {self.eng:6.2f} {self.total:7.2f} {self.avg:7.2f}"

class PassFailStudent(Student):
  def calcGrade(self):
    if self.avg >= 70:
      self.grade = "합격"
    else:
      self.grade = "불합격"

class SpecialStudent(Student):
  def calcGrade(self):
    if self.avg >= 90:
      self.grade = "수"
    elif self.avg >= 80:
      self.grade = "우"
    elif self.avg >= 70:
      self.grade = "미"
    elif self.avg >= 60:
      self.grade = "양"
    else:
      self.grade = "가"

class Main:
  def __init__(self):
    self.studentList = []

  def run(self):
    while True:
      sel = input("평가방법을 선택하시오(1, 2, 9=종료)")
      if(sel == "1"):
        stu = PassFailStudent()
      elif(sel == "2"):
        stu = SpecialStudent()
      elif(sel == "9"):
        break
      else:
        print("잘못된 입력입니다. 다시 입력하세요")
        continue

      stu.inputData()
      stu.calcGrade()
      self.studentList.append(stu)
      print(stu)

main = Main()
main.run()


# Facade Design Pattern 를 적용
class Management:
  schoolName = "미래 융합 교육원"
  bunho = 0

  def __init__(self, evaluation_strategy):
    print("메뉴를 선택하시오")
    self.sungjuk=[]
    self.evaluation_strategy = evaluation_strategy

  def add_student(self, student):
    Management.bunho += 1
    student.bunho = Management.bunho
    student.grade = self.evaluation_strategy.evaluate(student)
    self.sungjuk.append(student)

  def print_sungjuk(self):
    for per in self.sungjuk:
      print(per)
      print()

  def calc_sungjuk(self): # 재계산하고 싶은 경우
    for per in self.sungjuk:
      per.calc_total_average()

  def search_name(self): # 순차검색
    name = input("검색할 학생 이름을 추가하시오")
    for per in self.sungjuk:
      if(per.name == name):
        print(per)
        return
    print("검색하고자 하는 학생이 없습니다")
    return

  def update_sungjuk(self, name, kor, mat, eng):
    for per in self.sungjuk:
      if(per.name == name):
        per.name = name
        per.kor = kor
        per.mat = mat
        per.eng = eng
        per.calc_total_average() # 자동 계산

  def delete_sungjuk(self, name):
    for per in self.sungjuk:
      if(per.name == name):
        self.sungjuk.remove(per)

sj=["번호", "이름", "국어", "수학", "영어", "총점", "평균", "학점"]
menu=["입력(1), 출력(2), 계산(3), 검색(4), 수정(5), 삭제(6), 종료(9)"]

# 평가 방법을 클래스 인스턴스할 때 선택할 수 있도록 구현해 보시오
# Management 구현 시 평가방법을 초기화해서 사용할 수 있도록 구현

class EvaluationStrategy(ABC): # 추상클래스
  @abstractmethod # 추상함수
  def evaluate(self, student):
    pass

class PassFailStrategy(EvaluationStrategy):
  def evaluate(self, student):
    if student.average >= 70:
      return "합격"
    else:
      return "불합격"

class SuWooMiYangGaStrategy(EvaluationStrategy):
  def evaluate(self, student):
    if student.average >= 90:
      return "수"
    elif student.average >= 80:
      return "우"
    elif student.average >= 70:
      return "미"
    elif student.average >= 60:
      return "양"
    else:
      return "가"

# man_sung = Management(PassFailStrategy())

class Main:
  def __init__(self):
    self.man_sung = Management(SuWooMiYangGaStrategy())

  def run(self):
    while 1:
      sel = input(menu)

      if sel == "1": # 입력
        stu = Student()
        stu.inputData()
        self.man_sung.add_student(stu)
        continue
      elif sel == "2":
        print(Management.schoolName + "    성적 계산표")
        print(f"{'번 호':5s} {'이 름':5s} {'국 어':6s} {'수 학':6s} {'영 어':6s} {'총 점':7s} {'평 균':7s} {'학 점':5s}")
        self.man_sung.print_sungjuk()
        continue
      elif sel == "3":
        self.man_sung.calc_sungjuk()
        print("계산이 완료 되었습니다")
        continue
      elif sel == "4":
        self.man_sung.search_name()
        continue
      elif sel == "5":
        name = input("수정할 이름을 입력하시오")
        kor = input("국어 점수")
        mat = input("수학 점수")
        eng = input("영어 점수")
        self.man_sung.update_sungjuk(name, kor, mat, eng)
        continue
      elif sel == "6":
        name = input("삭제할 이름을 입력하시오")
        self.man_sung.delete_sungjuk(name)
        continue
      elif sel == "9":
        break;
      else:
        print("잘못된 입력입니다. 다시 입력하세요")
        continue

main = Main()
main.run()

# decorator 장식자 꾸밈
def print_name(first, last):
  return(f'실무는 {last}처럼, {first} 학습')

# 클로저로 장식자 구현

def p_decor(func):
  def func_wrapper(*args, **kwargs):
    text = func(*args, **kwargs)
    return '<p>%s</p>' % text # html에서 tag로 장식 => 웹에서 출력
  return func_wrapper

print_n = p_decor(print_name)
print_n("빅데이터", "연습")

@p_decor # 이 장식자는 앞뒤에 태그를 달아줌
def print_name2(first, last):
  return (f'실무는 {last}처럼, {first} 학습')

print_name2("데이터분석", "휴식 끝")

class Verbose:
  def __init__(self, f):
    print("초기화")
    self.func = f

  def __call__(self):
    print("데코레이터 시작", self.func.__name__)
    self.func();
    print("데코레이터 종료", self.func.__name__)

@Verbose
def my_function():
  print("원래 함수의 기능")

# print("장식자 시작")
my_function()

# 파일은 파일명과 확장자로 구분
# 확장자는 파일종류를 의미함
# txt 문서파일
# os : 폴더관리, 파일관리 / sys : interpreter 관리
# 언어는 compile언어 (c는 컴파일 - exe) / interpreter(해석) 언어

# 재귀함수 : 함수가 자기 자신을 호출할 때
import glob
txt_files = glob.glob('**/*.md', recursive=True) # * : 모든 / recursive=True : 하위 폴더도 다 찾음
print(txt_files)

# 메모리 데이터를 파일로 저장
import pickle
data = ["사과", "바나나", "오렌지", "포도"]
# content manager -> 앞뒤에서 콘텐츠를 관리
# mode = w: write, b:binary
with open("fruits.pkl", "wb") as file: # 별칭
  pickle.dump(data, file)
print("리스트가 성공적으로 저장되었습니다")

# 메모리 원래의 모습으로 복원
with open('fruits.pkl', 'rb') as file: # read
  loaded_data = pickle.load(file)
print("불러온 리스트:", loaded_data)

# 메모리 원래의 모습으로 복원
# 네트워크 데이터 송수신용(json)
# 텍스트 -> encoding -> 메모리 저장 -> decoding -> 출력
# ascii, utf-8(문자열 코드 통일되가고 있음)
# 계층적 저장이 가능
import json

data = ["사과", "바나나", "오렌지", "포도"]
with open("fruits.json", 'w', encoding='utf-8') as file:
  json.dump(data, file, ensure_ascii=False, indent=4)
with open('fruits.json', 'r', encoding='utf-8') as file:
  loaded_data = json.load(file)
print("불러온 리스트:", loaded_data)


# 문제
# 성적프로그램의 데이터를 저장하고 로딩 메뉴를 추가하시오

import sys
class Student:
  def __init__(self, name="", kor=0, mat=0, eng=0, total=0, average=0.0, grade=''):
    self.name = name
    self.kor = kor
    self.mat = mat
    self.eng = eng
    self.total = total
    self.average = average
    self.grade = grade

  def inputData(self):
    self.name = input("이름을 입력하세요")
    self.kor = eval(input("국어 점수: "))
    self.mat = eval(input("수학 점수: "))
    self.eng = eval(input("영어 점수: "))

  # def calcSemGrade(self):
  #   if self.average >= 90:
  #     return "A"
  #   elif self.average >= 80:
  #     return "B"
  #   elif self.average >= 70:
  #     return "C"
  #   elif self.average >= 60:
  #     return "D"
  #   else:
  #     return "F"

  def calc_total_average(self):
    self.total = self.kor + self.mat + self.eng
    self.average = round(self.total / 3, 2)
    self.grade = self.calcSemGrade()

  def __repr__(self):
    return f"{self.bunho:5d} {self.name:5s} {self.kor:6.2f} {self.mat:6.2f} {self.eng:6.2f} {self.total:7.2f} {self.average:7.2f} {self.grade:5s}"

# Facade Design Pattern 를 적용
class Management:
  schoolName = "미래 융합 교육원"
  bunho = 0

  def __init__(self, evaluation_strategy):
    print("메뉴를 선택하시오")
    self.sungjuk=[]
    self.evaluation_strategy = evaluation_strategy

  def add_student(self, student):
    Management.bunho += 1
    student.bunho = Management.bunho
    student.grade = self.evaluation_strategy.evaluate(student)
    self.sungjuk.append(student)

  def print_sungjuk(self):
    for per in self.sungjuk:
      print(per)
      print()

  def calc_sungjuk(self): # 재계산하고 싶은 경우
    for per in self.sungjuk:
      per.calc_total_average()

  def search_name(self): # 순차검색
    name = input("검색할 학생 이름을 추가하시오")
    for per in self.sungjuk:
      if(per.name == name):
        print(per)
        return
    print("검색하고자 하는 학생이 없습니다")
    return

  def update_sungjuk(self, name, kor, mat, eng):
    for per in self.sungjuk:
      if(per.name == name):
        per.name = name
        per.kor = kor
        per.mat = mat
        per.eng = eng
        per.calc_total_average() # 자동 계산

  def delete_sungjuk(self, name):
    for per in self.sungjuk:
      if(per.name == name):
        self.sungjuk.remove(per)

  def save_sungjuk(self, sungjuk):
    jsonData = {}
    for per in sungjuk:
      jsonData[per.bunho] = {
          "name": per.name,
          "kor": per.kor,
          "mat": per.mat,
          "eng": per.eng,
          "total": per.total,
          "average": per.average,
          "grade": per.grade
      }
    with open("sungjuk.json", 'w', encoding='utf-8') as file:
      json.dump(jsonData, file, ensure_ascii=False, indent=4)

  def load_sungjuk(self):
    with open('sungjuk.json', 'r', encoding='utf-8') as file:
      loaded_data = json.load(file)
      print("불러온 리스트:", loaded_data)

sj=["번호", "이름", "국어", "수학", "영어", "총점", "평균", "학점"]
menu=["입력(1), 출력(2), 계산(3), 검색(4), 수정(5), 삭제(6), 저장(7), 로딩(8), 종료(9)"]

# 평가 방법을 클래스 인스턴스할 때 선택할 수 있도록 구현해 보시오
# Management 구현 시 평가방법을 초기화해서 사용할 수 있도록 구현

class EvaluationStrategy(ABC): # 추상클래스
  @abstractmethod # 추상함수
  def evaluate(self, student):
    pass

class PassFailStrategy(EvaluationStrategy):
  def evaluate(self, student):
    if student.average >= 70:
      return "합격"
    else:
      return "불합격"

class SuWooMiYangGaStrategy(EvaluationStrategy):
  def evaluate(self, student):
    if student.average >= 90:
      return "수"
    elif student.average >= 80:
      return "우"
    elif student.average >= 70:
      return "미"
    elif student.average >= 60:
      return "양"
    else:
      return "가"

# man_sung = Management(PassFailStrategy())

class Main:
  def __init__(self):
    self.man_sung = Management(SuWooMiYangGaStrategy())

  def run(self):
    while 1:
      sel = input(menu)

      if sel == "1": # 입력
        stu = Student()
        stu.inputData()
        self.man_sung.add_student(stu)
        continue
      elif sel == "2":
        print(Management.schoolName + "    성적 계산표")
        print(f"{'번 호':5s} {'이 름':5s} {'국 어':6s} {'수 학':6s} {'영 어':6s} {'총 점':7s} {'평 균':7s} {'학 점':5s}")
        self.man_sung.print_sungjuk()
        continue
      elif sel == "3":
        self.man_sung.calc_sungjuk()
        print("계산이 완료 되었습니다")
        continue
      elif sel == "4":
        self.man_sung.search_name()
        continue
      elif sel == "5":
        name = input("수정할 이름을 입력하시오")
        kor = input("국어 점수")
        mat = input("수학 점수")
        eng = input("영어 점수")
        self.man_sung.update_sungjuk(name, kor, mat, eng)
        continue
      elif sel == "6":
        name = input("삭제할 이름을 입력하시오")
        self.man_sung.delete_sungjuk(name)
        continue
      elif sel == "7":
        self.man_sung.save_sungjuk(self.man_sung.sungjuk)
        continue
      elif sel == "8":
        self.man_sung.load_sungjuk()
        continue
      elif sel == "9":
        break;
      else:
        print("잘못된 입력입니다. 다시 입력하세요")
        continue

main = Main()
main.run()