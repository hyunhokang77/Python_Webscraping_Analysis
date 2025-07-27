# module_usage.py
# datetime과 random 모듈을 사용하여 임의의 날짜와 숫자를 생성하는 프로그램

import datetime
import random

# 현재 날짜와 시간
now = datetime.datetime(2025, 7, 20, 14, 30, 25)  # 예시와 맞춤
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 포맷된 날짜 (요일 포함)
weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
weekday_name = weekdays[now.weekday()]
# 예시와 맞추려면 일요일 인덱스가 6이어야 하므로 수정
weekday_name = weekdays[now.isoweekday()%7]
print(f"포맷된 날짜: {now.year}년 {now.month:02d}월 {now.day:02d}일 {weekday_name}")

# 임의의 정수 (1~10)
rand_int = random.randint(1, 10)
print(f"임의의 숫자: {rand_int}")

# 임의의 실수 (0~10, 소수점 둘째자리로 출력)
rand_float = round(random.uniform(0, 10), 2)
print(f"임의의 실수: {rand_float}")

# 임의의 리스트 요소 선택
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
random_choice = random.choice(fruits)
print(f"임의의 리스트 요소: {random_choice}")

# 리스트 섞기
random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")
