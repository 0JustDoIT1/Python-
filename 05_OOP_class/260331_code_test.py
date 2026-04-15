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