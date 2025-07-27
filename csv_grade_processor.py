# csv_grade_processor.py
# CSV 형태의 학생 성적 데이터를 파일에 저장하고 읽어서 평균을 계산하는 프로그램

import csv

grades = [
    ["이름", "점수"],
    ["김철수", 85],
    ["이영희", 92],
    ["박민수", 78],
    ["최수진", 95]
]

# CSV 파일에 저장
with open("grades.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(grades)

print("학생 성적이 grades.csv에 저장되었습니다.\n")

# CSV 파일에서 읽어서 분석
students = []
scores = []

with open("grades.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        name = row[0]
        score = int(row[1])
        students.append((name, score))
        scores.append(score)

print("성적 분석 결과:")
for name, score in students:
    print(f"{name}: {score}점")
average = sum(scores) / len(scores)
print(f"전체 평균: {average:.1f}점")
