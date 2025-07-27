# unpacking_example.py
# 언패킹과 *args, **kwargs 사용 예제

# 튜플 언패킹
coord = (10, 20)
x, y = coord
print(f"좌표: x={x}, y={y}")

# 리스트 언패킹
lst = [1, 2, 3]
a, b, c = lst
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# *args를 사용하는 함수
def sum_all(*args):
    return sum(args)

result = sum_all(10, 20, 30)
print(f"가변 인수의 합: {result}")

# **kwargs를 사용하는 함수
def print_kwargs(**kwargs):
    items = [f"{key}={value}" for key, value in kwargs.items()]
    print(f"키워드 인수들: {', '.join(items)}")

print_kwargs(name="김철수", age=25, city="서울")
