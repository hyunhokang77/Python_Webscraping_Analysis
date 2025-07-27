# 문자열을 입력받아 특정 문자가 몇 번 나타나는지 세는 프로그램

# 문자열 입력받기
text = input("문자열을 입력하세요: ")
char = input("찾을 문자를 입력하세요: ")

# 문자 등장 횟수 세기
count = text.count(char)

# 결과 출력
print(f"문자 '{char}'이 {count}번 나타납니다.")
