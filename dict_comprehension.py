# dict_comprehension.py
# 딕셔너리 컴프리헨션을 사용하여 숫자와 그 제곱값의 딕셔너리를 만드는 프로그램

# 1부터 5까지의 제곱 딕셔너리
squares_dict = {i: i ** 2 for i in range(1, 6)}
print(f"1부터 5까지의 제곱 딕셔너리: {squares_dict}")

# 짝수만의 제곱 딕셔너리 (2~10)
even_squares = {i: i ** 2 for i in range(2, 11, 2)}
print(f"짝수만의 제곱 딕셔너리: {even_squares}")
