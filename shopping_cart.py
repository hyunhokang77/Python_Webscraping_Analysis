# 쇼핑 카트를 딕셔너리로 구현하여 상품을 추가하고 총 가격을 계산하는 프로그램

# 상품 정보: 상품명 -> [수량, 개당 가격]
cart = {
    '사과': [2, 1000],
    '바나나': [3, 800],
    '오렌지': [1, 1500]
}

print("쇼핑 카트:")
total = 0
for item, (qty, price) in cart.items():
    item_total = qty * price
    total += item_total
    print(f"{item}: {qty}개 (개당 {price}원) = {item_total}원")

print(f"총 가격: {total}원")
