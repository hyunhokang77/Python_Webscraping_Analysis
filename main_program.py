# main_program.py

import math_operations

# 원의 넓이
r = 5
print(f"원의 넓이: {math_operations.circle_area(r):.2f}")

# 직사각형 넓이
w, h = 10, 5
print(f"직사각형 넓이: {math_operations.rectangle_area(w, h)}")

# 팩토리얼
n = 5
print(f"팩토리얼 {n}! = {math_operations.factorial(n)}")

# 최대공약수
a, b = 48, 18
print(f"최대공약수({a}, {b}) = {math_operations.gcd(a, b)}")
