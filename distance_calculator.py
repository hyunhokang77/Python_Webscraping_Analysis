# 좌표를 튜플로 저장하고 두 점 사이의 거리를 계산하는 프로그램

# 두 점 좌표 튜플로 저장
point1 = (0, 0)
point2 = (3, 4)

# 거리 계산 (피타고라스 공식)
distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

# 결과 출력
print(f"점1: {point1}")
print(f"점2: {point2}")
print(f"두 점 사이의 거리: {distance}")
