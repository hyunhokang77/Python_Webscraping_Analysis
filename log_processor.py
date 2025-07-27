# log_processor.py
# 로그 파일을 생성하고 특정 레벨의 로그만 필터링하여 출력하는 프로그램

log_filename = "system.log"

log_lines = [
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:00:00 - INFO - 백업 완료",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족",
    "2025-07-20 13:00:00 - INFO - 사용자 로그인"
]

# 로그 파일 생성
with open(log_filename, "w", encoding="utf-8") as f:
    for line in log_lines:
        f.write(line + "\n")

print("로그 파일이 생성되었습니다.\n")

# 로그 파일에서 특정 레벨의 로그만 필터링하여 출력
def print_logs_by_level(level):
    with open(log_filename, "r", encoding="utf-8") as f:
        filtered = [line.strip() for line in f if f"- {level} -" in line]
    print(f"{level} 레벨 로그들:")
    for line in filtered:
        print(line)
    print()

print_logs_by_level("ERROR")
print_logs_by_level("WARNING")
