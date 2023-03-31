
# 사용자에게 보여줄 메뉴화면을 실행하는 함수
def show_menu():
    print("\n*** 재고 관리 프로그램 ***")
    print("# 1. 제품 정보 등록하기")
    print("# 2. 모든 제품 정보 조회")
    print("# 3. 개별 제품정보 조회")
    print("# 4. 제품 정보 수정하기")
    print("# 5. 제품 정보 삭제하기")
    print("# 6. 프로그램 종료하기")
    
    menu = input("# 메뉴를 입력하세요: ")
    return menu

# 1번
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

# 2번
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

# 3번 메뉴 개별 제품조회를 수행할 함수
def search_product():
    print("# 조회하실 제품의 번호를 입력하세요.")
    code = input("# 제품번호를 입력하세요: ")

    for product in inventory: 
    #inventory를 반복문으로 돌리겠다. product안에 product1,2,3이 한번씩 들어온다.
        if code == product['제품번호']:
            print("\n            ***[%s] %s 재고정보***"
                   % product['제품번호'], product['제품명'])
            print("=" * 45)
            print("%s%10s%11s%12s%12s" % ("제품번호", "제품명", "단가", "수량", "제품총액"))
            print("=" * 45)
            print("%s%8s  %10d원%8d개    %9d원" 
              % (product['제품번호'], product['제품명'], product['단가'],
                 product['수량'], product['제품총액']))
            break
    
    else:
        print("해당하는 제품 정보가 등록되지 않았습니다.")
    # 제품 번호에 해당하는 제품 정보만 출력되도록 작성.
    # 사전에 해당 정보가 있는지 확인 후 있다면 해당 제품만 출력.
    
# 4번 메뉴 제품정보 수정을 수행할 함수.
def modify_product():
    print("수정할 제품의 코드를 입력하세요.")
    code = input("# 제품번호를 입력하세요: ")
                
    for product in inventory:
    if code == product['제품정보']:
        print("# [%s] %s 제품의 정보를 수정합니다." 
              % (product['제품번호'], product['제품명']))
        
        product['수량'] = int(input("- 수정할 수량: "))
        product['제품번호'] = 
        prodcut['제품총액'] = 
            
    # 제품 번호에 해당하는 제품의 단가와 수량을 선택적으로
    # 수정할 수 있도록 코드를 작성하세요. 
    # 수량 변경, 단가변경, 일괄변경을 작성하세요. (수량과 가격만 수정)
    
# 5번 메뉴 제품정보 삭제를 수행할 함수.
def delete_product():
    print("-삭제하실 제품의 번호를 입력하세요")
    code = input("-제품번호: ")
                
        if product in inventory:
        del(inventory[product])
            print("%s(이)가 삭제되었습니다." % name)
        else:
            print("%s(은)는 등록된 메뉴가 아닙니다." % name)
                
    # 리스트에서 사전 데이터를 통째로 삭제하여
    # 삭제가 완료된 후 제품의 조회가 불가능하도록 구성하세요.
    for product in inventory:
        if code == product['제품번호']
            print("# [%s] %s 제품의 정보를 삭제합니다." 
                  % (product['제품번호'], product['제품명']))
#        inventory.remove(prodcut)
            del(inventory[inventory.index(product)])
        
            print("\n %s의 정보삭제가 정상 처리되었습니다." % product['제품명'])
    else:
        print("해당하는 제품 정보가 등록되지 않았습니다.")
        
# 메뉴창을 수동으로 열게 하는 함수.
def program_continue():
    print("\n# 메뉴화면으로 돌아가시려면 Enter를 누르세요.")
    input()



inventory = []

while True:
    
    menu = show_menu()
    
    if menu == "1":
        insert_product()
    elif menu == "2":
        show_all_product()
    elif menu == "3":
        search_product()
    elif menu == "4":
        modify_product()
    elif menu == "5":
        delete_product()
    elif menu == "6":
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



