# ----------heidi SQL 구현-----------
# heidiSQL
# 데이터 베이스 생성 [OTT]
# table 생성 [review]
# 프로시저 생성 review_select_all,  review_select_one,  review_delete,  review_update,  review_insert

# === review_insert 프로시저 ===

# BEGIN
#     DECLARE exit handler FOR sqlexception
#     BEGIN
#         ROLLBACK;
#         SET result = -1;
#     END;
#     START TRANSACTION;
#         INSERT INTO review(content_title, user_name, rating, watch_date)
#         VALUES (p_content_title, p_user_name,p_rating,p_watch_date);
#         COMMIT;
#         SET result = 1;
# END



# === review_select_all 프로시저 ===

# BEGIN
#     SELECT * FROM review;
# END




# === review_select_one 프로시저 ===

# BEGIN
#     SELECT * FROM review WHERE content_title = p_content_title;
# END

# === review_update 프로시저 ===
# BEGIN
#     DECLARE cnt INT DEFAULT 0;
#     DECLARE exit handler FOR sqlexception
#     BEGIN
#         ROLLBACK;
#         SET result = -1;
#     END;
#     START TRANSACTION;
#     -- 검색 대상이 있는지 확인
#         SELECT COUNT(*) INTO CNT FROM review WHERE content_title = p_content_title;
#         if cnt > 0 then
#         UPDATE review SET rating = p_rating WHERE content_title = p_content_title;
#         SET result = 1; -- 업데이트 성공
#         COMMIT;
#     ELSE SET result =2; -- 찾는 데이터가 없음
#     END if;
# END

# === review_delete 프로시저 ===
# BEGIN
#     DECLARE cnt INT DEFAULT 0;

#     -- 에러 발생 시 처리
#     DECLARE exit handler FOR sqlexception
#     BEGIN
#         ROLLBACK;
#         SET result = -1; -- 삭제 중 에러
#     END;

#     START TRANSACTION;

#         -- 1. 삭제 대상 존재 여부 확인
#         SELECT COUNT(*) INTO cnt
#         FROM review
#         WHERE content_title = p_content_title;

#         if cnt > 0 then
#             -- 2.삭제 실행
#             DELETE FROM review
#             WHERE content_title = p_content_title;

#             COMMIT;
#             SET result = 1; -- 삭제성공
#         ELSE
#             -- 3. 대상 없음
#             ROLLBACK;
#             SET result =2; -- 삭제할 대상 없음
#         END if;

# END

# Python에서 MySQL DB를 관리하기 위한 라이브러리 가져오기
import pymysql
# 날짜 사용 라이브러리 가져오기
from datetime import date

# OTT 콘텐츠 리뷰 Class
class ReviewContents:
  # 시청 일자를 위한 오늘 날짜
  today = date.today()

  # 생성자 (콘텐츠 제목, 이름, 평점, 시청일자)
  def __init__(self, content_title="", user_name="", rating=0, watch_date=today):
    self.content_title = content_title
    self.user_name = user_name
    self.rating = rating
    self.watch_date = watch_date

  # 객체를 표현할 때 문자열로 출력되는 방식 수정
  def __repr__(self):
    return (
        f"[콘텐츠 정보]\n"
        f"제목      : {self.content_title}\n"
        f"이름      : {self.user_name}\n"
        f"평점      : {self.rating}\n"
        f"시청날짜  : {self.watch_date}"
    )


# Manager Class
# 리뷰 리스트 관리 및 MySQL 쿼리 실행 코드 관리
class Manager:
  # 생성자
  def __init__(self):
      # connect를 통해 MySQL 데이터베이스에 연결
      self.conn = pymysql.connect(
        host = '34.173.204.212',  # IP
        port = 3306,              # port (MySQL default = 3306)
        user = 'pressea1414',     # 사용자 계정
        password = 'jdHee9213@',  # 비밀번호
        database = 'OTT',         # DB 이름
        charset = 'utf8mb4',      # 문자 인코딩 방식
        autocommit = True,        # 자동 커밋 여부
        cursorclass = pymysql.cursors.DictCursor  # Dict 형태로 반환
      )
      # DB에 SQL을 보내고 결과를 받아오기 위한 커서(작업도구) 생성
      cur = self.conn.cursor()
      # DB에 해당 테이블이 없으면 생성, 있으면 그대로 무시
      # 즉, 사용하려는 테이블의 존재 여부 체크
      cur.execute("""
        CREATE TABLE IF NOT EXISTS review (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content_title VARCHAR(30),
            user_name VARCHAR(10),
            rating INT,
            watch_date DATE
        )
      """)
      # 리뷰 리스트 초기값에 전체 리뷰 리스트 할당
      self.reviewList = self.selectalldb()

  # 소멸자 - 객체가 삭제될 때 실행되는 정리 함수
  # 혹시나 객체 삭제가 되는 타이밍에 connect가 남아있다면 연결 끊기
  def __del__(self):
    try:
      if hasattr(self, "conn") and self.conn:
        self.conn.close()
    except Exception:
      pass

  # 객체 내에 데이터와 DB 간에 데이터 동기화 작업
  def checksync(self):
    # DB 데이터
    db_list = self.selectalldb()
    # 현재 객체 데이터
    mem_list = self.reviewList

    # dict 형태로 변환하기 위한 초기값 설정
    # -> for 문은 전체 데이터를 비교하기에는 불필요한 횟수가 많음
    # -> 따라서, dict 형태로 변환하여 key로 바로 비교하기 위함
    db_dict = {}
    mem_dict = {}

    # DB 데이터 : list => dict
    for dbdata in db_list:
      db_dict[dbdata.content_title] = dbdata
    # 객체 데이터 : list => dict
    for memdata in mem_list:
      mem_dict[memdata.content_title] = memdata

    # DB 데이터를 중심으로 비교 (DB가 정확한 데이터이기 때문에)
    # 1. items()를 활용해서 (key, dbdata) 형태로 변환
    # 2. 해당 타입은 튜플이기 때문에 반복문을 활용해서 비교
    for key, dbdata in db_dict.items():
      # 객체 데이터에 key가 없다면 데이터가 서로 다름 -> 동기화 작업 필요
      if key not in mem_dict:
        self.reviewList = db_list
        print("데이터 동기화 처리 완료")
        return
      else:
        # key는 있지만 데이터가 서로 다름 -> 동기화 작업 필요
        if db_dict[key] != mem_dict[key]:
          self.reviewList = db_list
          print("데이터 동기화 처리 완료")
          return
    # 둘 다 아니라면 이미 같은 데이터로 동기화되어 있는 경우
    print("데이터 동기화가 되어있습니다.")

  # 삽입
  def insertdb(self, content_title, user_name, rating, watch_date):
    cur = self.conn.cursor()
    # 프로시저 리턴(out) 파라미터 자리 필요
    # 콘텐츠 제목, 이름, 평점, 시청 일자, 리턴값
    params = (content_title, user_name, rating, watch_date, 0)
    # 프로시저 실행
    cur.callproc("review_insert", params)
    # review_insert 프로시저의 4번째 파라미터(OUT) 값 조회
    cur.execute('SELECT @_review_insert_4')
    # 결과 가져오기
    result = cur.fetchone()
    # 결과값이 Dict 형태로 오기 때문에 한번 더 key로 접근해서 꺼내야 함
    insertRes = result['@_review_insert_4']
    # 삽입 성공 (OUT == 1)
    if insertRes ==  1:
      rv = ReviewContents()
      rv.content_title = content_title
      rv.user_name = user_name
      rv.rating = rating
      rv.watch_date = watch_date
      # 객체 데이터에 동기화 작업을 위한 추가
      self.reviewList.append(rv)
      print(f"{content_title}에 대한 리뷰를 등록했습니다.")
    # 삽입 실패
    else:
      print("리뷰 등록 실패")
    # 연결은 항상 닫기
    cur.close()

  # 전체 조회
  def selectalldb(self):
    cur=self.conn.cursor()
    # 이미 생성한 프로시저를 통해 전체 조회
    cur.callproc("review_select_all")
    # 출력값을 담기 위한 빈 리스트 생성
    rvList = []
    # 결과값 받아오기
    result = cur.fetchall()
    # 받아온 데이터를 위에 만든 OTT 리뷰 객체 형태로 변환하고 리스트에 담음
    for review in result:
      rv = ReviewContents()
      rv.content_title = review['content_title']
      rv.user_name = review['user_name']
      rv.rating = review['rating']
      rv.watch_date = review['watch_date']
      rvList.append(rv) # 삽입
      print(rv) # 모든 객체 반복 출력해서 전체 리뷰 출력
    # 연결은 항상 닫기
    cur.close()
    # 전체 조회 데이터를 활용하기 위해 리턴으로 받음
    return rvList

  # 하나만 조회 (조건 : 콘텐츠 제목)
  def selectonedb(self, content_title):
    # ,를 활용해야 1개짜리 변수를 담은 튜플로 생성
    params = (content_title,)
    cur=self.conn.cursor()
    # 프로시저 활용
    cur.callproc("review_select_one", params)
    # 찾은 데이터 하나 반환
    result = cur.fetchone()
    if(result):
      # 마찬가지로 객체에 담아서 수정한대로 출력
      rv = ReviewContents()
      rv.content_title = result['content_title']
      rv.user_name = result['user_name']
      rv.rating = result['rating']
      rv.watch_date = result['watch_date']
      print(rv)
    else:
      print("찾으려는 콘텐츠가 없습니다.")
    # 연결은 항상 닫기
    cur.close()

  # 삭제(조건 : 콘텐츠 제목)
  def deletedb(self, content_title):
    # 프로시저 리턴(out) 파라미터 자리 필요
    params = (content_title, 0)
    cur = self.conn.cursor()
    # 프로시저 실행
    cur.callproc("review_delete", params)
    # review_delete 프로시저의 1번째 파라미터(OUT) 값 조회
    cur.execute ('SELECT @_review_delete_1')
    result= cur.fetchone()
    deleteRes = result["@_review_delete_1"]
    # 삭제 성공 (OUT == 1)
    if(deleteRes == 1):
      # 객체 데이터 동기화 작업을 위한 삭제
      # 리스트 컴프리헨션 + 조건문 활용
      # [표현식 for 변수 in 리스트 if 조건]
      self.reviewList = [
        r for r in self.reviewList
        if r.content_title != content_title
      ]
      print(f"{content_title}의 리뷰가 삭제되었습니다.")
    # 삭제할 콘텐츠가 존재하지 않는 경우 (OUT == 2)
    elif(deleteRes == 2):
      print("등록되지 않은 리뷰입니다.")
    # 삭제 처리 에러 (OUT == -1)
    elif(deleteRes == -1):
      print("삭제 실패")
    # 그 외 에러
    else:
      print("알 수 없는 에러")
    # 연결은 항상 닫기
    cur.close()

  # 수정 (조건 : 콘텐츠 제목 / 수정 Field : 평점)
  def updatedb(self, rating, content_title):
    # 프로시저 리턴(out) 파라미터 자리 필요
    params = (rating, content_title, 0)
    cur = self.conn.cursor()
    # 프로시저 실행
    cur.callproc("review_update", params)
    # review_update 프로시저의 2번째 파라미터(OUT) 값 조회
    cur.execute('SELECT @_review_update_2')
    result = cur.fetchone()
    updateRes = result["@_review_update_2"]
    # 수정 성공 (OUT == 1)
    if(updateRes == 1):
      # 객체 데이터 동기화 작업을 위한 수정
      # DB와 마찬가지로 제목을 조건으로 찾고 평점 수정
      for r in self.reviewList:
        if r.content_title == content_title:
          r.rating = rating
      print(f"{content_title}의 평점이 수정되었습니다.")
    # 수정할 콘텐츠가 존재하지 않는 경우 (OUT == 2)
    elif(updateRes == 2):
      print("등록되지 않은 리뷰입니다.")
    # 수정 처리 에러 (OUT == -1)
    elif(updateRes == -1):
      print("수정 실패")
    # 그 외 에러
    else:
      print("알 수 없는 에러")
    # 연결은 항상 닫기
    cur.close()

# Main Class
# 메뉴 관리 및 프린트 입력 관리
class Main:
  # 생성자
  def __init__(self):
      # Manager 객체 생성
      self.mgr = Manager()

  # 실제 실행을 위한 함수
  def run(self):
    # 무한 반복
    # 조건 종료 : '9' 입력
    while True:
      print("\n1.생성 2.전체 조회 3.이름 조회 4.평점 수정 5.삭제 6.동기화체크 9.종료")
      num = input("번호 선택: ")

      if num == '1':
        content_title = input("콘텐츠 제목 : ")
        name = input("이름 : ")
        rating = int(input("평점 : "))
        watch_date = input("시청날짜 (YYYY-MM-DD) : ")
        self.mgr.insertdb(content_title, name, rating, watch_date)
      elif num == '2':
        self.mgr.selectalldb()
      elif num == '3':
        content_title = input("콘텐츠 제목 : ")
        self.mgr.selectonedb(content_title)
      elif num == '4':
        content_title = input("콘텐츠 제목 : ")
        rating = input("새 평점 : ")
        self.mgr.updatedb(rating, content_title)
      elif num == '5':
        content_title = input("콘텐츠 제목 : ")
        self.mgr.deletedb(content_title)
      elif num == '6':
        self.mgr.checksync()
      elif num == '9':
          print("종료")
          break
      else:
          print("잘못 누름")


main=Main()
main.run()