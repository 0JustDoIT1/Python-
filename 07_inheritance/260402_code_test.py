# 주말 문제 (일요일 저녁)

# 1인분의 성적을 저장할 수 있는 클래스를 작성하시오 (기본 클래스)
# - 공통 규칙
# 리스트에 CRUD하는 manager class를 작성하시오
# menu를 작성해서 CRUD를 관리하는 main class를 작성하시오
# while문: 1.입력 2.출력 3.수정 4.삭제 5.정렬 6.등수 9.종료

# 학생 성적 클래스
class StudentScore:
  # 초기화 (이름, 국어, 영어, 수학)
  def __init__(self, name="", kor=0, eng=0, math=0):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math

  # 총점 계산
  def calcTotal(self):
    return self.kor + self.eng + self.math

  # 평균 계산
  def calcAverage(self):
    return round(self.calcTotal() / 3, 2) # 소수점 둘 째 자리까지

  # 출력을 위한 문자열 설정
  def __repr__(self):
    return (
        f"[{self.name}]\n"
        f" ┣ 국어: {self.kor}점\n"
        f" ┣ 영어: {self.eng}점\n"
        f" ┣ 수학: {self.math}점\n"
        f" ┣ 총점: {self.calcTotal()}점\n"
        f" ┗ 평균: {self.calcAverage():.2f}점"
    )

# CRUD를 위한 Manager 클래스
# Manager 클래스는 데이터 처리 기능만 보유(CRUD와 관련된 기능만)
# 검색 기준은 이름으로 임의 설정(이름은 Unique라고 가정)
class Manager:
  # 초기화 세팅
  def __init__(self):
    self.studentList = []

  # 이름 매개변수가 존재하는지 체크
  def checkArgsName(self, name):
    if(name is None): # 없으면 에러 처리
      raise ValueError("학생 이름을 확인하세요")

  # 생성
  def create(self, student):
    # 기존 리스트에 추가
    self.studentList.append(student)
    return student

  # 조회
  # 조회 - 전체 명단
  def readAll(self):
    return self.studentList

  # 조회 - 이름 검색으로 한 명만
  def readByName(self, name):
    # name 체크
    self.checkArgsName(name)
    # 아래 코드를 generator로 생성
    # next() 사용 - 첫 번째 값 반환(unique로 가정해서 상관x)
    #
    # for s in self.studentList:
    #   if(s.name == name):
    #     return s
    # return None
    return next((s for s in self.studentList if s.name == name), None)

  # 수정
  def update(self, student):
    # name 체크
    self.checkArgsName(student.name)

    # # 해당 학생을 찾고 업데이트
    # for s in self.studentList:
    #   if(s.name == student.name):
    #     s.kor = student.kor
    #     s.eng = student.eng
    #     s.math = student.math

    #     # print(f"{student.name} 학생 성적을 업데이트했습니다")
    #     return s
    # raise ValueError(f"{student.name} 학생은 존재하지 않습니다")

    # 학생 조회
    s = self.readByName(student.name) # 위에 만든 readByName 활용
    if(not s): # 값이 없으면 None 반환
      return None

    # 성적 업데이트
    s.kor = student.kor
    s.eng = student.eng
    s.math = student.math

    return s

  # 삭제
  def delete(self, name):
    # name 체크
    self.checkArgsName(name)
    # 학생 조회
    s = self.readByName(name) # 위에 만든 readByName 활용
    if(not s): # 값이 없으면 None 반환
      return None
    # 리스트에서 삭제
    self.studentList.remove(s)

    return s

# 사용자 인터페이스 및 메뉴 관리용 class
# 해당 인터페이스에서 입출력 관리
class Main:
  # 초기화에서 Manager 객체 생성해서 사용
  def __init__(self):
    self.manager = Manager()

  # 학생 이름 input 함수
  def getStudentName(self):
    name = input("학생 이름: ").strip() # 문자열 공백 제거
    return name

  # 학생 점수 input 함수
  def getStudentScore(self):
    try:
      kor = int(input("국어 점수: "))
      eng = int(input("영어 점수: "))
      math = int(input("수학 점수: "))
    except ValueError:
      raise ValueError("점수는 숫자로 입력해야 합니다")
    return kor, eng, math

  # 학생 이름 유효성 검사(간단하게만)
  def checkStudentName(self, name):
    # 이름 - 빈 값, 문자열
    if not name or not name.isalpha():
      return False
    return True

  # 학생 점수 유효성 검사(간단하게만)
  def checkStudentScore(self, kor, eng, math):
    # 점수 - 범위
    # 점수는 객체 생성 시 0점으로 초기값 생성
    # 0은 점수에서 유효한 값이기 때문에 빈 값 체크 따로 x
    for score in [kor, eng, math]:
      if not (0 <= score <= 100):
        return False
    return True

  # 학생 생성 - 입출력
  def addStudent(self):
    # 이름 입력 및 검사
    name = self.getStudentName()
    if(not self.checkStudentName(name)):
      print("학생 이름을 정확히 입력해 주세요")
      return
    # 점수 입력 및 검사
    kor, eng, math = self.getStudentScore()
    if not self.checkStudentScore(kor, eng, math):
      print("점수는 0~100 사이로 입력해 주세요")
      return
    # 학생 객체 생성
    student = StudentScore(name, kor, eng, math)
    # Create 실행
    result = self.manager.create(student)
    print(result)

  # 학생 조회 - 입출력
  def readStudent(self):
    name = self.getStudentName()
    # 이름 검색 (즉, 한 명 조회)
    if(name):
      result = self.manager.readByName(name) # readByName 실행
      if(result):
        print(result)
      else:
        print(f"{name} 학생은 존재하지 않습니다")
    # 전체 검색
    else:
      resultList = self.manager.readAll() # readAll 실행
      if(resultList):
        for s in resultList:
          print(s)
          print("-" * 30)
      else:
        print("등록된 학생이 없습니다")

  # 학생 수정 - 입출력
  def updateStudent(self):
    # 이름 입력 및 검사
    name = self.getStudentName()
    if(not self.checkStudentName(name)):
      print("학생 이름을 정확히 입력해 주세요")
      return
    # 학생 존재여부 체크
    existCheck = self.manager.readByName(name)
    if not existCheck:
      print(f"{name} 학생은 존재하지 않습니다")
      return
    # 점수 입력 및 검사
    kor, eng, math = self.getStudentScore()
    if not self.checkStudentScore(kor, eng, math):
      print("점수는 0~100 사이로 입력해 주세요")
      return
    # 학생 객체 생성
    student = StudentScore(name, kor, eng, math)
    # Update 실행
    result = self.manager.update(student)
    print(f"{result.name} 학생 성적을 수정했습니다")
    print(result)

  # 학생 삭제 - 입출력
  def deleteStudent(self):
    # 이름 입력 및 검사
    name = self.getStudentName()
    if(not self.checkStudentName(name)):
      print("학생 이름을 정확히 입력해 주세요")
      return
    # 학생 존재여부 체크
    existCheck = self.manager.readByName(name)
    if not existCheck:
      print(f"{name} 학생은 존재하지 않습니다")
      return
    # Delete 실행
    result = self.manager.delete(name)
    print(f"{result.name} 학생 성적을 삭제했습니다")

  # 메뉴로 관리
  def run(self):
    while True:
      print("\n===== 성적 관리 프로그램 =====")
      print("1. 입력")
      print("2. 출력")
      print("3. 수정")
      print("4. 삭제")
      print("9. 종료")

      # menu = int(input("메뉴 선택: "))
      try:
        menu = int(input("메뉴 선택: "))
      except ValueError: # 숫자 아닌 값 입력 처리
        print("숫자를 입력해 주세요")
        continue

      if menu == 1:
          self.addStudent()
      elif menu == 2:
          self.readStudent()
      elif menu == 3:
          self.updateStudent()
      elif menu == 4:
          self.deleteStudent()
      elif menu == 9:
          print("프로그램 종료")
          break
      else:
          print("잘못된 입력입니다")
          continue



menu = Main()
menu.run()