
'''
* 사전을 사용한 음식점 메뉴판 관리 프로그램
- key: 음식명, value: 음식의 가격
'''
foods = {}

while True:
    
    print("\n\n====== 음식점 메뉴 관리 프로그램 ======")
    print("# 1. 신규 메뉴 등록하기")
    print("# 2. 메뉴판 전체보기")
    print("# 3. 프로그램 종료하기")
    print("====================================")
    menu = input("# 메뉴 입력: ")
    
    if menu == "1":
        # 1. 메뉴명을 입력받아 해당 메뉴가 사전에 이미 존재한다면
        # "이미 등록된 메뉴입니다" 를 출력하세요.
        # 2. 사전에 존재하지 않는 메뉴(key)라면 가격을 입력받아
        # key : value쌍으로 맵핑하여 사전에 저장하세요.
        name = input("메뉴명: ")
        if name not in foods:
            price = input("가격: ")
            foods[name] = price
            print("신규 메뉴 %s(이)가 등록되었습니다." % name)
        else:
            print("%s(은)는 이미 등록된 메뉴입니다." % name)
        
        
    elif menu == "2":
        if len(foods) != 0:
            
            print("\n======= 메뉴판 =======")
            for m in foods:
                print("%s : %s원" % (m, foods[m]))
            print("======================")
            print("1. 수정 | 2. 삭제 | 3. 나가기")
            select = input("=> ")
            
            if select == "1":
                print("가격을 변경할 메뉴의 이름을 입력하세요.")
                name = input("=> ")
                
                if name in foods:
                    newprice = input("변경할 가격: ")
                    foods[name] = newprice
                    print("%s의 가격이 %s원으로 변경되었습니다." 
                          % (name, newprice))
                else:
                    print("%s(은)는 등록된 메뉴가 아닙니다." % name)
                
            elif select == "2":
                # 삭제할 메뉴명을 입력받아서 삭제를 진행하세요.
                # 없는 메뉴를 입력했을 시 등록되지 않은 메뉴라고
                # 출력해 주세요.
                print("삭제할 메뉴명을 입력하세요")
                name = input("=> ")
                
                if name in foods:
                    del(foods[name])
                    print("%s(이)가 삭제되었습니다." % name)
                else:
                    print("%s(은)는 등록된 메뉴가 아닙니다." % name)
                
        else:
            print("메뉴부터 먼저 입력해 주세요!")

    elif menu == "3":
        print("# 프로그램을 종료하시겠습니까? [Y/N]")
        choice = input("=> ")
        if choice[0].lower() == "y":
            print("프로그램을 종료합니다.")
            break
        else:
            print("종료를 취소합니다.")
            continue
    else:
        print("메뉴를 잘못 입력했습니다.")
        
    print("\n메뉴를 보시려면 Enter를 입력하세요...")
    input()
    
    
    
    
    
    
    
    
    



