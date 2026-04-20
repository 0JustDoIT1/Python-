# 문제2) (팀 문제 제출용)
# 다음과 같은 벡터를 정규화하고 단위벡터(방향)를 출력하시오
# A1 = [3,4,2,5,6]
# B1 = [1,1,1,2,2]
# 이 문제는 위의 3차원을 수정해서 다차원이 가능하도록 구현해야 함
# x,y,z가 아니라 리스트로 입력 받아 처리하면 차원에 상관없이 처리가 가능

import math

class Vector:
  # 생성자
  # 값을 list 형태로 받음
  def __init__(self, vectorList):
    self.vectorList = vectorList

  # 더하기
  def __add__(self,other):
    addList = []
    # 차원(리스트 길이)이 같을 때만 처리
    if(len(self.vectorList) == len(other.vectorList)):
      # 어차피 차원(index)이 같은 값끼리 계산하기 때문에 똑같은 index 사용
      for i in range(len(self.vectorList)):
        vectorAdd = self.vectorList[i] + other.vectorList[i]
        addList.append(vectorAdd)
    return Vector(addList)

  # 곱하기
  def __mul__(self,other):
    mulList = []
    # 차원(리스트 길이)이 같을 때만 처리
    if(len(self.vectorList) == len(other.vectorList)):
      # 어차피 차원(index)이 같은 값끼리 계산하기 때문에 똑같은 index 사용
      for i in range(len(self.vectorList)):
        vectorMul = self.vectorList[i] * other.vectorList[i]
        mulList.append(vectorMul)
    return Vector(mulList)

  # 빼기
  def __sub__(self,other):
    subList = []
    # 차원(리스트 길이)이 같을 때만 처리
    if(len(self.vectorList) == len(other.vectorList)):
      # 어차피 차원(index)이 같은 값끼리 계산하기 때문에 똑같은 index 사용
      for i in range(len(self.vectorList)):
        vectorSub = self.vectorList[i] - other.vectorList[i]
        subList.append(vectorSub)
    return Vector(subList)

  # 나누기
  def __truediv__(self,other):
    divList = []
    # 차원(리스트 길이)이 같을 때만 처리
    if(len(self.vectorList) == len(other.vectorList)):
      # 어차피 차원(index)이 같은 값끼리 계산하기 때문에 똑같은 index 사용
      for i in range(len(self.vectorList)):
        vectorDiv = self.vectorList[i] / other.vectorList[i]
        divList.append(vectorDiv)
    return Vector(divList)

  # 몫만 구하기
  def __floordiv__(self,other):
    floorList = []
    # 차원(리스트 길이)이 같을 때만 처리
    if(len(self.vectorList) == len(other.vectorList)):
      # 어차피 차원(index)이 같은 값끼리 계산하기 때문에 똑같은 index 사용
      for i in range(len(self.vectorList)):
        vectorFloor = self.vectorList[i] // other.vectorList[i]
        floorList.append(vectorFloor)
    return Vector(floorList)

  # 출력을 위한 str 전환
  def __repr__(self):
    return f"{self.vectorList}"

  # 하나의 벡터 크기
  def norm(self):
    sum = 0
    for i in range(len(self.vectorList)):
      sum += self.vectorList[i]**2
    return math.sqrt(sum)

  # 벡터 정규화 - 단위 벡터 구하기
  def normalize(self):
    normalizeList=[]
    # 벡터 크기 값이 구해짐
    dist = self.norm()
    # 각 좌표에 대한 계산 필요
    for i in range(len(self.vectorList)):
      normalizeList.append(self.vectorList[i] / dist)
    return Vector(normalizeList)

  # 두 벡터의 크기(거리) 구하기
  def dist(self,other):
    sum = 0
    for i in range(len(self.vectorList)):
      sum += (self.vectorList[i] - other.vectorList[i])**2
    return math.sqrt(sum)

  # 내적
  def dot(self,other):
    sum = 0
    for i in range(len(self.vectorList)):
      sum += (self.vectorList[i] * other.vectorList[i])
    return sum

  # 코사인 유사도 = <A,B> / |A||B|
  def cosangle(self, other):
    dot = self.dot(other) # 내적
    norm1 = self.norm() # 크기
    norm2 = other.norm() # 크기
    return dot / (norm1 * norm2)

  # 각도 구하기
  def theta(self,other):
    cosangle = self.cosangle(other)
    # 원주율은 3.141592
    # math.acos(cosangle) -> 라디안 값
    return math.acos(cosangle) * (180 / math.pi)


A1 = Vector([1,2,3,3,3,6,6])
B1 = Vector([1,2,3,3,2,3,1])

print(f"A1 벡터의 크기: \t{A1.norm()}")
print(f"B1 벡터의 크기: \t{B1.norm()}")

print(f"A1의 단위 벡터: \t{A1.normalize()}")
print(f"B1의 단위 벡터: \t{B1.normalize()}")

print(f"두 벡터의 내적: \t{A1.dot(B1)}")
print(f"두 벡터의 cos: \t\t{A1.cosangle(B1)}")
print(f"두 벡터의 각도: \t{A1.theta(B1)}")