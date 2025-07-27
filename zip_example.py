# zip_example.py
# zip을 사용하여 두 리스트를 결합하는 프로그램

students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

print("학생과 점수 매칭:")
for name, score in zip(students, scores):
    print(f"{name}: {score}점")

# 점수별 학생 딕셔너리 만들기
score_dict = dict(zip(students, scores))
print(f"점수별 학생 딕셔너리: {score_dict}")
