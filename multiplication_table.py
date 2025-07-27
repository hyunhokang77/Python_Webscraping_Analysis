# 구구단을 출력하는 프로그램 (사용자가 입력한 단만 출력)

dan = int(input("몇 단을 출력할까요? "))

print(f"{dan}단 구구단:")
for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")
