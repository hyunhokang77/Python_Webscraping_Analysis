# 원의 반지름을 입력받아 넓이와 둘레를 계산하는 프로그램

# 파이 값 지정
pi = 3.14159

# 반지름 입력받기
radius = float(input("원의 반지름을 입력하세요: "))

# 넓이와 둘레 계산
area = pi * radius * radius
circumference = 2 * pi * radius

# 결과 출력 (소수점 둘째 자리까지)
print(f"반지름이 {int(radius)}인 원의 넓이: {area:.2f}")
print(f"반지름이 {int(radius)}인 원의 둘레: {circumference:.2f}")
