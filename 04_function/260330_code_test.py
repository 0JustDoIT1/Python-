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

# 학생 수
student_num = 3

# 입력함수
def getStudentData():
  classList = [] # 반 list 초기화 선언
  # 세번 입력받기 위해 반복
  for i in range(student_num):
    name = input("이름: ")
    kor = int(input("국어: "))
    eng = int(input("영어: "))
    math = int(input("수학: "))
    studentData = [name, kor, eng, math] # 학생 한명의 기본 성적 데이터
    classList.append(studentData) # 반 list에 학생 데이터 추가
  return classList

# 학생별 총점, 평균 계산함수
def calcSumAvg(classList):
  # 학생 수만큼 for문 (여기서 student는 값)
  for student in classList:
    sum = student[1] + student[2] + student[3] # 총점
    avg = round(sum / 3, 2) # 평균 (반올림, 소수점 2째 자리까지 표현)
    student.append(sum) # 각 학생 데이터에 총점 및 평균 추가
    student.append(avg)


# 학점함수
def calcGrade(classList):
  # 학생 수만큼 for문
  for student in classList:
    # 임의의 기준을 통해서 구분
    if(student[4] >= 270): grade = 'A'
    elif(student[4] >= 240): grade = 'B'
    elif(student[4] >= 210): grade = 'C'
    elif(student[4] >= 180): grade = 'D'
    elif(student[4] >= 150): grade = 'E'
    else: grade = 'F'
    student.append(grade)

# 석차함수
def calcRank(classList):
  # 총점을 기준으로 미리 내림차순 정렬
  classList.sort(key=lambda s:int(s[4]), reverse=True)
  # 학생 수만큼 for문
  for student in classList:
    # 등수 초기값 선언 (1등)
    rank = 1
    # 다른 학생과 비교하기 위해 이중 for문
    for student2 in classList:
      # 점수가 낮을 경우에만 등수가 밀려야되기 때문에 +1
      # 점수가 같거나 높을 경우에는 현재 설정된 rank에서 변동 X
      if(student[4] < student2[4]):
        rank += 1
    student.append(rank)

# 반 총점/평균 함수
def calcClassSumAvg(classList):
  # 총점 계산을 위한 초기값 선언
  classSum = 0
  for student in classList:
    classSum += student[4]
  # 반올림, 소수점 2째 자리까지 표현
  classAvg = round(classSum / len(classList), 2)

  # 문제에서 따로 리스트에 추가할 필요 없어보여서 출력을 위해 return만 받음
  return (classSum, classAvg)


# 출력함수
# f-string 활용
def printScoreList(classList, classSum, classAvg):
  print("="*40)
  print("[반 성적]")
  print(f"총점 : {classSum}점")
  print(f"평균 : {classAvg}점")
  print("="*40)

  for student in classList:
    print(f"[{student[7]} 등]")
    print(f"이름   : {student[0]}")
    print(f"학점   : {student[6]}")
    print(f"총점   : {student[4]}점")
    print(f"평균   : {student[5]}점")
    print("-"*40)
    print("[과목별 점수]")
    print(f"  국어 : {student[1]}점")
    print(f"  영어 : {student[2]}점")
    print(f"  수학 : {student[3]}점")
    print("="*40)

# 최종 실행 함수
def main():
  scoreList = getStudentData()
  calcSumAvg(scoreList)
  calcGrade(scoreList)
  calcRank(scoreList)
  (classSum, classAvg) = calcClassSumAvg(scoreList)
  printScoreList(scoreList, classSum, classAvg)

main()
