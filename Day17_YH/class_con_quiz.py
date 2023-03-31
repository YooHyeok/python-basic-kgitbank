

'''
1. Account 라는 클래스를 선언하세요.

2. 생성자를 정의하세요. (은행이름, 예금주, 비밀번호)
생성자를 정의할 때 계좌 잔액을 표시할 수 있는 
변수를 생성하세요. (balance)

3. 입금기능을 가진 메서드를 선언하세요.

4. 출금기능을 가진 메서드를 선언하세요.
'''
class Account:
    def __init__(self, bank, owner, password, balance):
        self.balance = 0
        self.bank = bank
        self.owner = owner
        self.password = password
        
    def deposit(self, money):
        self.balance += money
    
    def withdraw(self, money):
        self.balance += money
        
        
#     def user_info(self):
#         print(self.bank,"은행 계좌 잔액:", self.balance, "원")
#         print("[예금주:",self.owner , "비밀번호:",self.password,"]")
        
woori = Account("우리", "홍길동", 1234)
woori.deposit(10000)
woori.withdraw(4300)

print("%s 은행 계좌 잔액: %d원" % (woori.bank, woori.balance))

print("[예금주: %s님, 비밀번호: %d" % (woori.owner, woori.password))



























