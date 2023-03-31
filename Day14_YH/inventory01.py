# -재고관리 프로그램-
# 제품 1개당 필요한 정보
# [제품번호, ,제품명, 단가, 수량, 제품총액]

product1 = {"제품번호" : "a001",
            "제품명" : "냉장고",
            "단가" : 500000,
            "수량" : 4,
            "제품총액" : 2000000
            }

product2 = {"제품번호" : "a002",
            "제품명" : "에어컨",
            "단가" : 700000,
            "수량" : 6,
            "제품총액" : 4200000
            }

product3 = {"제품번호" : "a003",
            "제품명" : "청소기",
            "단가" : 300000,
            "수량" : 9,
            "제품총액" : 2700000
            }

inventory = [product1, product2, product3]

print("-" * 40)

code = input("# 제품번호를 입력하세요: ")

for product in inventory: 
    #inventory를 반복문으로 돌리겠다. product안에 product1,2,3이 한번씩 들어온다.
    if code == product['제품번호']:
        print("조회하신 제품의 이름은 %s입니다" % product['제품명'])
        break
    
else:
    print("등록되지 않은 제품입니다.")
















