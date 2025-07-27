# 문자열을 입력받아 대문자, 소문자, 길이를 출력하는 프로그램

# 문자열 입력받기
text = input("문자열을 입력하세요: ")

# 변환 및 길이 계산
uppercase = text.upper()
lowercase = text.lower()
length = len(text)

# 결과 출력
print(f"대문자: {uppercase}")
print(f"소문자: {lowercase}")
print(f"문자열 길이: {length}")
