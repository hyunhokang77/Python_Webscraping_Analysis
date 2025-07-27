# 직사각형의 가로와 세로 길이를 입력받아 넓이와 둘레를 계산하는 프로그램

# 가로, 세로 입력받기
width = int(input("가로 길이를 입력하세요: "))
height = int(input("세로 길이를 입력하세요: "))

# 넓이와 둘레 계산
area = width * height
perimeter = 2 * (width + height)

# 결과 출력
print(f"직사각형의 넓이: {area}")
print(f"직사각형의 둘레: {perimeter}")