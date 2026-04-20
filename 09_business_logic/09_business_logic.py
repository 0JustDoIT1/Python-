# DB연결 소켓관리는 os (한계가 있어서 연결거부)
# DB와의 대화는 pymysql
import pymysql
connection = pymysql.connect(
    # 5가지 정보
    host='104.198.27.181',
    port=3306, # Default값
    user='hbc3869',
    password='Zmfjszl123!',
    database='test_db',
    charset='utf8mb4',
    autocommit=False
)
cursor = connection.cursor()
try: # 예외처리 (이상 감지) -> 프로그램은 중단없이 실행되야 함
  cursor.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)", ("대한민국", 30))
  connection.commit()
  print("데이터가 성공적으로 삽입되었습니다.")
except Exception as e: # 예외의 최상위 개체 (모든 예외 처리)
  connection.rollback()
  print("에러가 발생하여 롤백되었습니다.", e)
finally:
  cursor.close() # 객체 삭제
  connection.close()

import pymysql
conn = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True
)

try:
  # with 사용하고 나면 자동으로 정리(close)
  with conn.cursor() as cur: # content manager(시작, 종료)
    cur.execute("SELECT * FROM student")
    # recordset 생성
    rows = cur.fetchall() # list
    desc = cur.description # field 정의
    for row in rows: # 한 row씩 추출
      print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}')
finally:
  conn.close()

print(rows)
print(desc)

import pymysql
conn = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True
)

try:
  # with 사용하고 나면 자동으로 정리(close)
  with conn.cursor() as cur: # content manager(시작, 종료)
    cur.execute("SELECT * FROM student")
    # recordset 생성
    rows = cur.fetchone() # list
    print(f'{rows[0]}, {rows[1]}, {rows[2]}, {rows[3]}, {rows[4]}')
    rows = cur.fetchone() # list
    print(f'{rows[0]}, {rows[1]}, {rows[2]}, {rows[3]}, {rows[4]}')
finally:
  conn.close()

print(rows)

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True
)

try:
  cursor = connection.cursor()
  cursor.execute(
      "SELECT * FROM student WHERE bunho = %s", (1)
  )
  result = cursor.fetchone()
  print(result)
  connection.commit()
# mysql에서 발생하는 예외최상위 객체
# pymysql.err.OperationalError
except pymysql.MySQLError as e:
  print(f"Error: {e}")
  connection.rollback()
finally:
  cursor.close()
  connection.close()

# 문제
# student 테이블 select 쿼리한 다음 결과를
# 필드 이름이 상단에 출력되고 그에 맞추어서 결과를 출력하시오

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True
)

try:
  cursor = connection.cursor()
  cursor.execute(
      "SELECT bunho, name, kor FROM student"
  )
  result = cursor.fetchall()
  desc = cursor.description
  # 열 이름
  print (f"{desc[0][0]:<8} {desc[1][0]:<11} {desc[2][0]:<10}")
  for row in result:
    print(f"{row[0]:<8} {row[1]:<8} {row[2]:<10}")
except pymysql.MySQLError as e:
  print(f"Error: {e}")
  connection.rollback()
finally:
  cursor.close()
  connection.close()

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True
)

person = ("typoon", 100, 100, 100, "CH00000001")

try:
  with connection.cursor() as cur:
    cur.execute(
        "INSERT INTO student(name,kor,mat,eng,schoolcode) VALUES(%s,%s,%s,%s,%s)",
        (person[0], person[1], person[2], person[3], person[4])
    )
    conn.commit()
    print("새로운 학생이 등록되었습니다.")
finally:
  connection.close()

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True
)

try:
  with connection.cursor() as cur:
    cur.execute(
        "UPDATE student SET name = %s WHERE name = %s",
        ('korea', 'typoon')
    )
    conn.commit()
    print("학생 이름이 korea로 변경되었습니다.")
finally:
  connection.close()

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True
)

try:
  with connection.cursor() as cur:
    cur.execute(
        "DELETE FROM student WHERE name = %s",
        ('korea')
    )
    conn.commit()
    print("학생 데이터가 삭제되었습니다.")
finally:
  connection.close()

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True
)

try:
  with connection.cursor() as cur:
    cur.callproc("student_select") # recordset 생성
    if(cur.rowcount): # 영향을 미친 행 수
      print(cur.fetchall())
finally:
  connection.close()

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor
)

data=('둔산골', 90, 80, 100, 'CH00000000', 0)

try:
  with connection.cursor() as cur:
    cur.callproc("student_insert", data)
    # 내부적으로 결정이 되는 이름
    cur.execute("SELECT @_student_insert_5")
    connection.commit()
    result = cur.fetchone()
    print(result['@_student_insert_5'])
finally:
  connection.close()

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor
)

data=('전공삼', '삼성', 0)

try:
  with connection.cursor() as cur:
    cur.callproc("student_update", data)
    cur.execute("SELECT @_student_update_2")
    connection.commit()
    result = cur.fetchone()
    sel = result['@_student_update_2']
    print(sel)
    if(sel == 2):
      print("수정할 이름이 없습니다")
    elif(sel == -1):
      print("수정할 이름이 없습니다")
    elif(sel == 0):
      print("수정할 이름이 없습니다")
    else:
      print("알 수 없음")
finally:
  connection.close()

# 문제
# 삼성을 삭제하도록 procdure 호출로 구현해보시오
#

import pymysql
connection = pymysql.connect(
    host='104.198.27.181',
    port=3306,
    user='hbc3869',
    password='Zmfjszl123!',
    database='daejeon',
    charset='utf8',
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor
)

data = ("삼성", 0)

try:
  with connection.cursor() as cur:
    cur.callproc("student_delete", data)
    cur.execute("SELECT @_student_delete_1")
    connection.commit()
    result = cur.fetchone()
    dele = result['@_student_delete_1']
    print(dele)
    if(dele == 1):
      print("삭제 성공")
    elif(dele == 2):
      print("삭제할 대상 없음")
    elif(dele == -1):
      print("삭제 중 에러")
    else:
      print("알 수 없음")
finally:
  connection.close()

# 문제
# 테이블 구조
# 데이터베이스 : test_db / 테이블 : users
# 1. id int autoincrement
# 2. email varchar(50)
# 3. password varchar(30)
# 수정은 패스워드 수정으로
# stored procedure로 CRUD를 작성하시오
# pymysql을 이용해서 CRUD를 구현하시오

import pymysql

# cur.execute(
#     "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(50), password VARCHAR(30))"
#     )

DB_CONFIG = {
    "host": "104.198.27.181",
    "port": 3306,
    "user": "hbc3869",
    "password": "Zmfjszl123!",
    "database": "test_db",
    "charset": "utf8",
    "autocommit": True,
    "cursorclass": pymysql.cursors.DictCursor
}

# DB 연결
def getConnection():
  return pymysql.connect(**DB_CONFIG)

# 조회
def selectUsers():
  try:
    connection = getConnection()
    with connection.cursor() as cur:
      cur.callproc("users_select")
      if(cur.rowcount):
        print(cur.fetchall())

  finally:
    connection.close()

# 삽입
def insertUsers(email, password):
  try:
    connection = getConnection()
    data = (email, password, 0)
    with connection.cursor() as cur:
      cur.callproc("users_insert", data)
      cur.execute("SELECT @_users_insert_2")
      result = cur.fetchone()
      insertRes = result['@_users_insert_2']
      if(insertRes == 1):
        print("추가 성공")
      elif(insertRes == -1):
        print("추가 실패")
      else:
        print("알 수 없음")

      connection.commit()
  finally:
    connection.close()

# 수정
def updateUsers(email, password):
  try:
    data = (email, password, 0)
    connection = getConnection()
    with connection.cursor() as cur:
      cur.callproc("users_update", data)
      cur.execute("SELECT @_users_update_2")
      result = cur.fetchone()
      updateRes = result['@_users_update_2']
      print(updateRes)
      if(updateRes == 1):
        print("업데이트 성공")
      elif(updateRes == 2):
        print("찾는 데이터가 없음")
      elif(updateRes == -1):
        print("업데이트 에러")
      else:
        print("알 수 없음")

      connection.commit()
  finally:
    connection.close()

# 삭제
def deleteUsers(email):
  try:
    data = (email, 0)
    connection = getConnection()
    with connection.cursor() as cur:
      cur.callproc("users_delete", data)
      cur.execute("SELECT @_users_delete_1")
      result = cur.fetchone()
      delRes = result['@_users_delete_1']
      print(delRes)
      if(delRes == 1):
        print("삭제 성공")
      elif(delRes == 2):
        print("삭제할 대상 없음")
      elif(delRes == -1):
        print("삭제 중 에러")
      else:
        print("알 수 없음")

      connection.commit()
  finally:
    connection.close()

# insertUsers("test@test.com", "test1234")
# selectUsers()
# updateUsers("test@test.com", "test0000")
# deleteUsers("test@test.com")

class Student :
    def __init__(self):
        self.bunho=0
        self.name =''
        self.kor = 0;
        self.mat = 0
        self.eng = 0
        self.total = 0
        self.average=0
        self.grade=""
    def inputData(self):
        self.name = input("이름을 입력하세요")
        self.kor = eval(input("국어 점수:"))
        self.mat = eval(input("수학점수:"))
        self.eng = eval(input("영어점수 :"))

    def calc_total_average(self):
        self.total = self.kor + self.mat + self.eng
        self.average = round( self.total / 3, 2)
        self.grade = self.calcSemGrade()
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
    def __str__(self):
        return '%5s  %5s  %6s  %6s  %6s  %7s  %7s  %s' % (self.bunho, self.name, self.kor, self.mat,
                            self.eng, self.total, self.average, self.grade)
    def __cmp__(self, other): # 이름비교(클래스 == 클래스)
        return self.name == other.name
    def __call__(self, other ): # 2차원 리스트
        st=[]
        for student in other:
            stp = Student()
            stp.bunho = student[0]
            stp.name = student[1]
            stp.kor = student[2]
            stp.eng = student[3]
            stp.mat = student[4]
            st.append(stp)
        return st # 클래스 리스트

import pymysql

class MariaDB:
  DB_CONFIG = {
    "host": "104.198.27.181",
    "port": 3306,
    "user": "hbc3869",
    "password": "Zmfjszl123!",
    "database": "daejeon",
    "charset": "utf8",
    "autocommit": True,
    # "cursorclass": pymysql.cursors.DictCursor
  }

  def __init__(self):
    self.conn = pymysql.connect(**MariaDB.DB_CONFIG)
    cur = self.conn.cursor()
    cur.execute("SHOW TABLES")
    tables = cur.fetchall()
    print("###", tables)
    c = []
    for i in tables:
      if i == ('sungjuk',):
        c.append(i)
    if len(c) != 0: # 해당 테이블이 있으면
      sungjuk_table = "SELECT * FROM sungjuk"
      cur.execute(sungjuk_table)
      print("Table Check OK!")
    else:
      cur.execute(
          "CREATE TABLE sungjuk(name VARCHAR(20), kor INTEGER(20), mat INTEGER(20), eng INTEGER(20), total INTEGER(20), average INTEGER(20), grade CHAR(1))"
      )
      print("Create Table sungjuk")
    cur.close()

  def __del__(self): # 소멸자
    try:
      if hasattr(self, "conn") and self.conn:
        self.conn.close() # 초기화 안된 상태에서 close 하면 에러 발생
    except Exception:
      pass

  def selectdb(self):
    cur = self.conn.cursor()
    cur.callproc("student_select")
    st=[]
    if(cur.rowcount):
      stu_select = list(cur.fetchall())
      for student in stu_select:
        stp = Student()
        stp.bunho = student[0]
        stp.name = student[1]
        stp.kor = student[2]
        stp.eng = student[3]
        stp.mat = student[4]
        stp.total = student[5]
        stp.average = student[6]
        stp.grade = student[7]
        st.append(stp)
    else:
      st = []
    cur.close()
    return st

  def insertdb(self, in_name, in_kor, in_mat, in_eng):
    cur = self.conn.cursor()
    args = (in_name, in_kor, in_mat, in_eng, 'CH00000001', 0)
    cur.callproc("student_insert", args)
    cur.execute("SELECT @_student_insert_5")
    result = cur.fetchone()
    cur.close()
    return result

  def updatedb(self, in_name, up_name):
    cur = self.conn.cursor()
    args = (in_name, up_name, 0)
    cur.callproc("student_update", args)
    cur.execute("SELECT @_student_update_2")
    result = cur.fetchone()
    cur.close()
    return result

  def deletedb(self, in_name):
    cur = self.conn.cursor()
    args = (in_name, 0)
    cur.callproc("student_delete", args)
    cur.execute("SELECT @_student_delete_1")
    result = cur.fetchone()
    cur.close()
    return result

maria = MariaDB()
sts = maria.selectdb() # 클래스 리스트로 리턴
for st in sts:
  print(st)
ret=maria.deletedb("둔산골")
print(ret)