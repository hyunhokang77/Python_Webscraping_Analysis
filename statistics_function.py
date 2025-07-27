# statistics_function.py
# 리스트의 통계 정보(평균, 최댓값, 최솟값, 표준편차)를 반환하는 함수

def get_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)
    # 표준편차 계산 (모집단 기준)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = variance ** 0.5
    return mean, max_value, min_value, std_dev

# 예시 데이터
nums = [10, 20, 30, 40, 50]
mean, max_value, min_value, std_dev = get_statistics(nums)

print(f"숫자들: {nums}")
print(f"평균: {mean}")
print(f"최댓값: {max_value}")
print(f"최솟값: {min_value}")
print(f"표준편차: {std_dev:.2f}")
