# 문제1) (개인 제출)
# 추천을 하려고 한다
# [공포, 코미디, 액션] 영화에 대한 선호도가 다음과 같을 때
# 코사인 유사도를 0 ~ 1 사이의 값을 출력하시오
# 사용자 A = [5,1,0]
# 사용자 B = [4,2,1]

import math

# 영화 선호도 Class
class MoviePreference:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  # 더하기
  def __add__(self, other):
    return MoviePreference(self.x + other.x, self.y + other.y, self.z + other.z)
  # 곱하기
  def __mul__(self, other):
    return MoviePreference(self.x * other.x, self.y * other.y, self.z * other.z)
  # 빼기
  def __sub__(self, other):
    return MoviePreference(self.x - other.x, self.y - other.y, self.z - other.z)
  # 나누기
  def __truediv__(self, other):
    return MoviePreference(self.x / other.x, self.y / other.y, self.z / other.z)
  # 몫만 구하기
  def __floordiv__(self, other):
    return MoviePreference(self.x // other.x, self.y // other.y, self.z // other.z)
  # 출력을 위한 str 전환
  def __repr__(self):
    return f"공포 선호도={self.x}, 코미디 선호도={self.y}, 액션 선호도={self.z}"
  # 하나의 벡터 크기
  def norm(self):
    return math.sqrt(self.x**2 + self.y**2 + self.z**2)
  # 벡터 정규화 - 단위 벡터 구하기
  def normalize(self):
    dist = self.norm()
    return MoviePreference(self.x / dist, self.y / dist, self.z / dist)
  # 두 벡터의 크기(거리) 구하기
  def dist(self, other):
    return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
  # 내적
  def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z
  # 코사인 유사도
  def cosangle(self, other):
    dot = self.dot(other)
    norm1 = self.norm()
    norm2 = other.norm()
    return dot / (norm1 * norm2)
  # 각도
  def theta(self, other):
    cosangle = self.cosangle(other)
    return math.acos(cosangle) * (180 / math.pi)

A = MoviePreference(5,1,0)
B = MoviePreference(4,2,1)
print(f"A 선호도: \t{[5,1,0]}")
print(f"B 선호도: \t{[4,2,1]}")
print(f"A,B의 코사인 유사도: \t{A.cosangle(B)}")