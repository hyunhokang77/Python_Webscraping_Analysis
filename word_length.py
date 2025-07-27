# 단어들이 담긴 리스트에서 가장 긴 단어와 가장 짧은 단어를 찾는 프로그램

words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

print(f"단어 목록: {words}")

# 가장 긴 단어와 짧은 단어 찾기
longest = max(words, key=len)
shortest = min(words, key=len)

print(f"가장 긴 단어: {longest} ({len(longest)}글자)")
print(f"가장 짧은 단어: {shortest} ({len(shortest)}글자)")
