
inventory = []

for x in range(2): #[0,1]
    
    product = {}

    print("\n# 제품 정보 등록을 시작합니다.")
    product['제품번호'] = input("- 제품번호: ")
    product['제품명'] = input("- 제품명: ")
    product['단가'] = int(input("- 단가: "))
    product['수량'] = int(input("- 수량: "))
    product['제품총액'] = product['단가'] * product['수량']
    
    inventory.append(product)
    print("\n# 제품 등록이 정상 처리되었습니다.")


print("\n             *** 창고 재고 정보 ***")
print("=" * 45)
print("%s%10s%11s%12s%12s" % ("제품번호", "제품명", "단가", "수량", "제품총액"))
print("=" * 45)

for product in inventory:   
    print("%s%8s  %10d원%8d개    %9d원" 
        % (product['제품번호'], product['제품명'], product['단가'],
           product['수량'], product['제품총액']))
      
    print("=" * 45)

