# 과일 이름들이 담긴 리스트에서 특정 과일을 검색하는 프로그램

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print(f"과일 목록: {fruits}")
search = input("찾을 과일을 입력하세요: ")

if search in fruits:
    print(f"'{search}'가 목록에 있습니다!")
else:
    print(f"'{search}'가 목록에 없습니다.")
