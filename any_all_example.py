# any_all_example.py
# any와 all 함수를 사용하여 조건을 검사하는 프로그램

numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

# numbers1 검사
print(f"숫자 리스트: {numbers1}")
print(f"모든 수가 짝수인가? {all(num % 2 == 0 for num in numbers1)}")
print(f"하나라도 10보다 큰 수가 있는가? {any(num > 10 for num in numbers1)}\n")

# numbers2 검사
print(f"숫자 리스트2: {numbers2}")
print(f"모든 수가 짝수인가? {all(num % 2 == 0 for num in numbers2)}")
print(f"하나라도 10보다 큰 수가 있는가? {any(num > 10 for num in numbers2)}")
