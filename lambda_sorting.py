# lambda_sorting.py
# 람다 함수를 사용하여 리스트를 다양한 방식으로 정렬하는 프로그램

students = [
    ('김철수', 85),
    ('이영희', 92),
    ('박민수', 78),
    ('최수진', 95)
]

print(f"학생 정보: {students}")

# 이름순 정렬
sorted_by_name = sorted(students, key=lambda x: x[0])
print(f"이름순 정렬: {sorted_by_name}")

# 점수순 정렬 (오름차순)
sorted_by_score = sorted(students, key=lambda x: x[1])
print(f"점수순 정렬: {sorted_by_score}")

# 점수 내림차순 정렬
sorted_by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"점수 내림차순: {sorted_by_score_desc}")
