# 문장을 입력받아 공백을 제거하고, 단어의 개수를 세는 프로그램

# 문장 입력받기
sentence = input("문장을 입력하세요: ")

# 앞뒤/중복 공백 제거(단어 사이 공백은 하나로)
cleaned = ' '.join(sentence.split())

# 단어 개수 세기
word_count = len(cleaned.split())

# 결과 출력
print(f"공백 제거: {cleaned}")
print(f"단어 개수: {word_count}개")
