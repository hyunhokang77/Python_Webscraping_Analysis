# map_filter_example.py
# map과 filter를 사용하여 리스트를 처리하는 프로그램

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"원본 숫자: {numbers}")

# 모든 수의 제곱
squared = list(map(lambda x: x ** 2, numbers))
print(f"모든 수의 제곱: {squared}")

# 5보다 큰 수들
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"5보다 큰 수들: {greater_than_5}")

# 5보다 큰 수들의 제곱
squared_greater_than_5 = list(map(lambda x: x ** 2, greater_than_5))
print(f"5보다 큰 수들의 제곱: {squared_greater_than_5}")
