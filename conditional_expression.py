# conditional_expression.py

# 점수에 따라 결과를 결정하는 삼항 연산자
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

# 나이에 따라 상태를 결정하는 조건부 표현식
age = 17
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")

# 숫자 리스트에서 최대값 구하기 (조건부 표현식)
numbers = [5, 12, 8, 23, 42, -7, 0, -3]
max_value = numbers[0] if numbers else None
for n in numbers:
    max_value = n if n > max_value else max_value
print(f"숫자들의 최대값: {max_value}")

# 양수만 리스트에서 추출 (리스트 컴프리헨션과 조건부 표현식)
positives = [n for n in numbers if n > 0]
print(f"양수들: {positives}")
