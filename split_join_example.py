# split_join_example.py
# split과 join을 사용하여 문자열을 분리하고 다시 합치는 예제

text = "Python is awesome programming language"

# 단어별로 분리
words = text.split()

# 결과 출력
print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")

# 하이픈(-)으로 연결
hyphen_joined = "-".join(words)
print(f"하이픈으로 연결: {hyphen_joined}")

# 대문자로 변환 후 공백으로 연결
upper_joined = " ".join([word.upper() for word in words])
print(f"대문자로 변환 후 공백으로 연결: {upper_joined}")
