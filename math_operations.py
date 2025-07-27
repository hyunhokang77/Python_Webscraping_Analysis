# math_operations.py

PI = 3.14159

def circle_area(radius):
    return PI * radius * radius

def rectangle_area(width, height):
    return width * height

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
