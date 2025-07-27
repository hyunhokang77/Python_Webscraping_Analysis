# 중복된 요소가 있는 리스트에서 중복을 제거하고 정렬하는 프로그램

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(f"원본 리스트: {numbers}")

# 중복 제거 및 정렬
unique_sorted = sorted(set(numbers))

print(f"중복 제거 후: {unique_sorted}")
