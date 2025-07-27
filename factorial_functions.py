# factorial_functions.py
# 팩토리얼을 계산하는 재귀함수와 반복문 함수

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 테스트
for num in [5, 7]:
    print(f"{num}! (재귀) = {factorial_recursive(num)}")
    print(f"{num}! (반복) = {factorial_iterative(num)}")
