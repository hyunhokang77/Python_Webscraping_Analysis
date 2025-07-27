# 두 개의 리스트를 병합하고 공통 요소를 찾는 프로그램

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(f"리스트1: {list1}")
print(f"리스트2: {list2}")

# 리스트 병합 (중복 제거)
merged = sorted(set(list1 + list2))

# 공통 요소 찾기
common = sorted(set(list1) & set(list2))

print(f"병합된 리스트: {merged}")
print(f"공통 요소: {common}")
