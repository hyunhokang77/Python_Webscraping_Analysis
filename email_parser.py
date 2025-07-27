# 이메일 주소를 입력받아 사용자명과 도메인을 분리하는 프로그램

# 이메일 입력받기
email = input("이메일 주소를 입력하세요: ")

# @ 기호를 기준으로 분리
username, domain = email.split('@')

# 결과 출력
print(f"사용자명: {username}")
print(f"도메인: {domain}")
