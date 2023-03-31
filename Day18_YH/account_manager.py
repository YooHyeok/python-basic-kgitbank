
class Account:
    def __init__(self, bank, owner, password):
        self.balance = 0
        self.bank = bank
        self.owner = owner
        self.pw = password
        
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        self.balance -= money



my_acc = Account("우리", "박영희", 1234)
# 1번 메뉴: 계좌 정보를 조회하는 기능.
def account_info():
    print("*** 나의 계좌 정보***")
    print("은행명: %s은행" % my_acc.bank)
    print("예금주명: %s" % my_acc.owner)
    print("잔액 정보: %d원" % my_acc.balance)

# 2번 메뉴 : 입금기능
def deposit_acc():
    password = int(input("비밀번호를 입력:"))

    # 입력받은 비번이 통장비번과 일치하면 입금액을 받아서
    # 입금메서드를 통해 통장에 돈을 입금시키는 로직을 작성하세요.
    if password == my_acc.pw:
        money = int(input("입금액: "))
        my_acc.deposit(money)
        print("입금이 완료되었습니다.")
    else:
        print("비밀번호가 틀렸습니다.")

# 3번 메뉴: 출금 기능
def withdraw_acc():
    password = int(input("비밀번호를 입력: "))
    
    # 입력 받은 비번이 통장 비번과 일치하면 출금액을 다시 입력받아
    # 출금 멧드를 통해 통장에 돈을 출금시키세요.
    # 단, 현재 잔액보다 출금액이 크다면 "잔액이 부족합니다."를 출력하고
    # 출금을 실행하지 않습니다.
    if password == my_acc.pw:
        money = int(input("출금액: "))
        if my_acc.balance >= money:
            my_acc.withdraw(money)
            print("출금이 완료되었습니다.")
        else:
            print("잔액이 %d원 부족합니다." % (money - my_acc.balance))
    else:
        print("비밀번호가 틀렸습니다.")
 
# 4번 메뉴: 잔액조회
def check_acc():   
    print()
    print("잔액 정보: %d원" % my_acc.balance)
    
    
    
def menu_info():
    
    print("\n*** 계좌 관리 프로그램 ***")
    print("# 1. 계좌 정보 조회")
    print("# 2. 입금하기")
    print("# 3. 출금하기")
    print("# 4. 잔액조회")
    print("# 5. 프로그램 종료")

while True:
    
    menu_info()
    try:
        menu = int(input("메뉴: "))
    except:
        print("메뉴는 숫자로만 입력하세요!")
        continue

    if menu == 1:
        account_info()
    elif menu == 2:
        deposit_acc()
    elif menu == 3:
        withdraw_acc()
    elif menu == 4:
        check_acc()
    elif menu == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print()























