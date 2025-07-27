# 섭씨 온도를 입력받아 화씨 온도로 변환하는 프로그램

# 섭씨 온도 입력받기
celsius = float(input("섭씨 온도를 입력하세요: "))

# 화씨로 변환
fahrenheit = celsius * 9 / 5 + 32

# 결과 출력
print(f"섭씨 {int(celsius)}도는 화씨 {fahrenheit:.1f}도입니다.")
