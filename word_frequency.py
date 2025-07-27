# word_frequency.py
# 텍스트 파일의 단어 빈도를 계산하는 프로그램

filename = "sample_text.txt"

# 예시 텍스트 파일 내용 작성 (파일이 없으면 생성)
sample_lines = [
    "파이썬 프로그래밍 언어",
    "파이썬은 배우기 쉬운 언어입니다",
    "파이썬은 강력한 프로그래밍 언어입니다"
]

# sample_text.txt 파일에 예시 내용 저장
with open(filename, "w", encoding="utf-8") as f:
    for line in sample_lines:
        f.write(line + "\n")

# 단어 빈도 계산
word_count = {}

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        words = line.strip().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

# 빈도 내림차순으로 정렬
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

print("단어 빈도 분석 결과:")
for word, count in sorted_word_count:
    print(f"{word}: {count}번")
