# json_handler.py
# JSON 형태의 데이터를 파일에 저장하고 읽어오는 프로그램

import json

# 저장할 데이터 (딕셔너리 형태)
data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

# JSON 파일로 저장
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("데이터가 data.json에 저장되었습니다.\n")

# JSON 파일에서 읽어오기
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("JSON에서 읽어온 데이터:")
print(f"이름: {loaded_data['이름']}")
print(f"나이: {loaded_data['나이']}")
print(f"직업: {loaded_data['직업']}")
print(f"취미: {loaded_data['취미']}")
print(f"주소: {loaded_data['주소']}")
