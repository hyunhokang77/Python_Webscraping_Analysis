# 1부터 100까지 3의 배수의 합을 구하는 프로그램

# 3의 배수 리스트 생성
multiples_of_3 = [i for i in range(1, 101) if i % 3 == 0]

# 합계와 개수 계산
total = sum(multiples_of_3)
count = len(multiples_of_3)

# 결과 출력
print(f"1부터 100까지 3의 배수: {multiples_of_3}")
print(f"3의 배수의 합: {total}")
print(f"3의 배수의 개수: {count}개")
