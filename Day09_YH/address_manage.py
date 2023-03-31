
# 리스트를 활용한 연락처 관리 프로그램 구현.

namelist = []
phonelist = []

while True:
    print("\n--------연락처 관리 프로그램---------")
    print("1. 연락처 등록")
    print("2. 연락처 검색")
    print("3. 연락처 삭제")
    print("4. 모든 연락처 등록")
    print("5. 프로그램 종료")
    print("----------------------------------")
    
    menu = int(input("메뉴를 입력하세요: "))
    
    if menu == 1:
        
        print("-" * 20)
        print("연락처 등록을 시작합니다.")
        name = input("이름: ")
        phone = input("전화번호: ")

        # 입력받은 이름데이터와 전화번호 데이터를 각각의 리스트에 추가하세요
        # 추가 완료시 "xxx님 연락처 저장 완료!"를 출력하세요.
        namelist.append(name)
        phonelist.append(phone)
        
        print("%s님 연락처 저장 완료!" % name)
        
    elif menu == 2:
        
        name = input("찾을 이름을 입력하세요: ")
        
        # 입력한 이름이 리스트 안에서 발견된다면 해당 이름을 통해
        # 인덱스 번호를 추출하여 인덱스를 통해 리스트의 데이터를 출력합니다.
        # 출력예시: "홍길동의 전화번호는 010-1234-1234입니다."
        if name in namelist:
            idx = namelist.index(name)
            print("%s 님의 전화번호는  %s 입니다." 
                  % (name, phonelist[idx]))
        else:
            print("%s님은 연락처 목록에 없습니다.")
        
    elif menu == 3:
            name = input("삭제할 이름을 입력하세요: ")
            
            if name in namelist:
                idx = namelist.index(name)
                del namelist[idx]
                del phonelist[idx]
                print("%s님의 정보가 정상적으로 삭제되었습니다." % name)
            else:
                print("%s님은 연락처 목록에 없습니다." % name)
        
    elif menu == 4:
            print("========전체 연락처 조회========")
            # for문을 통해 리스트 내부의 모든 인덱스에 접근하여 모든 이름과
            # 연락처 정보를 출력하는 코드를 작성합니다.
        
#             for name in namelist:
#                 print(name, ":", phonelistp[namelist.index(name)])
            for idx in range(len(namelist)):
                print(namelist[idx], ":", phonelist[idx])
    elif menu == 5:
            print("프로그램을 종료합니다.")
            break
        
    else:
        print("메뉴를 다시 입력해주세요")
        