import math

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
  def __mul__(self, other):
    return Vector(self.x * other.x, self.y * other.y)
  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y)
  def __truediv__(self, other): # float 연산 소수점
    return Vector(self.x / other.x, self.y / other.y)
  def __floordiv__(self, other): # 몫만
    return Vector(self.x // other.x, self.y // other.y)
  def __repr__(self):
    return f"x좌표={self.x}, y좌표={self.y}"

  # 벡터의 크기(norm, length) 계산
  # √(x^2 + y^2)
  def norm(self):
    return math.sqrt(self.x**2 + self.y**2)
  # 벡터 정규화: 방향만 남기고 크기 1로 변환
  def normalize(self):
    dist = self.norm()
    return Vector(self.x / dist, self.y / dist)
  # 두 벡터(점) 사이 거리
  # √((x1-x2)^2 + (y1-y2)^2)
  def dist(self, other):
    return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
  # 벡터 내적(dot product)
  # A·B = x1*x2 + y1*y2
  # 방향 유사도와 크기 정보를 모두 반영
  def dot(self, other):
    return self.x * other.x + self.y * other.y
  # 코사인 유사도: 방향만 비교
  # cosθ = (A·B) / (|A||B|)
  def cosangle(self, other): # cosangle = <A,B> / |A||B|
    dot = self.dot(other)
    norm1 = self.norm()
    norm2 = other.norm()
    return dot / (norm1 * norm2)
  # 두 벡터 사이 각도 θ (도 단위)
  # math.acos()는 라디안 반환, 도 단위로 변환
  def theta(self, other):
    cosangle = self.cosangle(other)
    # 원주율은 3.141592
    # math.acos(cosangle) 라디안
    return math.acos(cosangle) * (180 / math.pi)


# 두 벡터의 내적이 0이면 사이각은 직교
# 직교 좌표계
f = Vector(10,1)
g = Vector(1,27)
print(f)
print(f + f)
print(f + g)
print(f * g)
print(f / g)
print(21.2 / 10.2)

print(f"f벡터의 크기= {f.norm()}")
print(f"g벡터의 크기= {g.norm()}")
print(f"f의 normal vector= {f.normalize()}")
print(f"g의 normal vector= {g.normalize()}")
print(f"두 벡터의 내적= {f.dot(g)}")
print(f"두 벡터의 cos= {f.cosangle(g)}")
print(f"두 벡터의 각도= {f.theta(g)}")

# 문제
# 3차원으로 확장하시오

import math

class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
  def __mul__(self, other):
    return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
  def __truediv__(self, other): # float 연산 소수점
    return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
  def __floordiv__(self, other): # 몫만
    return Vector(self.x // other.x, self.y // other.y, self.z // other.z)
  def __repr__(self):
    return f"x좌표={self.x}, y좌표={self.y}, z좌표={self.z}"
  def norm(self): # 벡터의 크기값
    return math.sqrt(self.x**2 + self.y**2 + self.z**2)
  def normalize(self): # 벡터 정규화
    dist = self.norm()
    return Vector(self.x / dist, self.y / dist, self.z / dist)
  def dist(self, other):
    return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
  def dot(self, other): # 내적
    return self.x * other.x + self.y * other.y + self.z * other.z
  def cosangle(self, other): # cosangle = <A,B> / |A||B|
    dot = self.dot(other)
    norm1 = self.norm()
    norm2 = other.norm()
    return dot / (norm1 * norm2)
  def theta(self, other): # 각도로 출력
    cosangle = self.cosangle(other)
    # 원주율은 3.141592 라디안
    # math.acos(cosangle) 라디안
    return math.acos(cosangle) * (180 / math.pi)

a = Vector(10,1,2)
b = Vector(1,27,2)

print(f"a벡터의 크기= {a.norm()}")
print(f"b벡터의 크기= {b.norm()}")
print(f"a의 normal vector= {a.normalize()}")
print(f"b의 normal vector= {b.normalize()}")
print(f"두 벡터의 내적= {a.dot(b)}")
print(f"두 벡터의 cos= {a.cosangle(b)}")
print(f"두 벡터의 각도= {a.theta(b)}")

# 문제1) (개인 제출)
# 추천을 하려고 한다
# [공포, 코미디, 액션] 영화에 대한 선호도가 다음과 같을 때
# 코사인 유사도를 0~1 사이의 값을 출력하시오
# 사용자 A = [5,1,0]
# 사용자 B = [4,2,1]

import math

class MoviePreference:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def __add__(self, other):
    return MoviePreference(self.x + other.x, self.y + other.y, self.z + other.z)
  def __mul__(self, other):
    return MoviePreference(self.x * other.x, self.y * other.y, self.z * other.z)
  def __sub__(self, other):
    return MoviePreference(self.x - other.x, self.y - other.y, self.z - other.z)
  def __truediv__(self, other):
    return MoviePreference(self.x / other.x, self.y / other.y, self.z / other.z)
  def __floordiv__(self, other):
    return MoviePreference(self.x // other.x, self.y // other.y, self.z // other.z)
  def __repr__(self):
    return f"공포 선호도={self.x}, 코미디 선호도={self.y}, 액션 선호도={self.z}"
  def norm(self):
    return math.sqrt(self.x**2 + self.y**2 + self.z**2)
  def normalize(self):
    dist = self.norm()
    return Vector(self.x / dist, self.y / dist, self.z / dist)
  def dist(self, other):
    return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
  def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z
  def cosangle(self, other):
    dot = self.dot(other)
    norm1 = self.norm()
    norm2 = other.norm()
    return dot / (norm1 * norm2)
  def theta(self, other):
    cosangle = self.cosangle(other)
    return math.acos(cosangle) * (180 / math.pi)

A = MoviePreference(5,1,0)
B = MoviePreference(4,2,1)
print(f"A 선호도= {[5,1,0]}")
print(f"B 선호도= {[4,2,1]}")
print(f"두 벡터의 cos= {A.cosangle(B)}")

# 문제2) (팀 문제 제출용)
# 다음과 같은 벡터를 정규화하고 단위벡터(방향)를 출력하시오
# A1 = [3,4,2,5,6]
# B1 = [1,1,1,2,2]
# A2 =
# 이 문제는 위의 3차원을 수정해서 다차원이 가능하도록 구현해야 함
# x,y,z가 아니라 리스트로 입력 받아 처리하면 차원에 상관없이 처리가 가능