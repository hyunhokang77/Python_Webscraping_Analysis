# file_write_read.py
# 텍스트 파일에 여러 줄의 문자열을 저장하고 읽어오는 프로그램

filename = "sample.txt"
lines = [
    "안녕하세요",
    "파이썬 파일 처리를 연습하고 있습니다",
    "오늘은 좋은 날씨입니다"
]

print("파일에 저장할 내용:")
for line in lines:
    print(line)

# 파일에 쓰기
with open(filename, "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

print("\n파일에서 읽어온 내용:")
# 파일에서 읽기
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
