
# 사용자에게 보여줄 메뉴화면을 실행하는 함수
def show_menu():
    print("\n*** 재고 관리 프로그램 ***")
    print("# 1. 제품 정보 등록하기")
    print("# 2. 모든 제품 정보 조회")
    print("# 3. 프로그램 종료하기")
    
    menu = input("# 메뉴를 입력하세요: ")
    return menu

# 1번메뉴: 제품 정보 등록을 수행할 함수.
def insert_product():
    product = {}
    
    print("\n# 제품 정보 등록을 시작합니다.")
    product['제품번호'] = input("- 제품번호: ")
    product['제품명'] = input("- 제품명: ")
    product['단가'] = int(input("- 단가: "))
    product['수량'] = int(input("- 수량: "))
    product['제품총액'] = product['단가'] * product['수량']
    
    inventory.append(product)
    print("\n# 제품 등록이 정상 처리되었습니다.")
    program_continue()
    
    
# 메뉴창을 수동으로 열게 하는 함수.
def program_continue():
    print("\n# 메뉴화면으로 돌아가시려면 Enter를 누르세요.")
    input()



# 2번 메뉴: 전체 조회를 수행할 함수
def show_all_product():
    all_price = 0 # 창고 재고의 전체 가격을 담아줄 변수.
    print("\n             *** 창고 재고 정보 ***")
    print("=" * 45)
    print("%s%10s%11s%12s%12s" % ("제품번호", "제품명", "단가", "수량", "제품총액"))
    print("=" * 45)

    for product in inventory:
        all_price += product['제품총액']
        print("%s%8s  %10d원%8d개    %9d원" 
              % (product['제품번호'], product['제품명'], product['단가'],
                 product['수량'], product['제품총액']))
    print("=" * 45)
    print("\t\t\t 창고 전체 제품 총액: %d원" % all_price)
    program_continue()


inventory = []

while True:
    
    menu = show_menu()
    
    if menu == "1":
        insert_product()
    elif menu == "2":
        show_all_product()
    elif menu == "3":
        print("# 프로그램을 종료합니다. [Y/N]")
        choice = input("=> ").lower()[0]
        if choice == "y":
            print("종료되었습니다.")
            break
        elif choice == "n":
            continue
        else:
            print("잘못 입력하셨습니다.")
    else:
        print("메뉴를 다시 입력하세요.")

