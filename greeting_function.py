# greeting_function.py
# 기본값 매개변수를 사용하여 인사말을 생성하는 함수

def greeting(name, message="안녕하세요", postfix="님!"):
    print(f"{message}, {name}{postfix}")

# 함수 호출 예시
greeting("김철수")
greeting("John", message="Hello", postfix="!")
greeting("이영희", message="안녕하세요", postfix="님! 좋은 하루 되세요!")
