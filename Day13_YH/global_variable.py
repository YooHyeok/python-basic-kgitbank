
'''
* 전역변수 (global variable)

- 지역변수가 함수 내부에서만 사용되는 변수라면
 전역변수는 프로그램 전체에서 사용되는 공용 변수입니다.

- 파이썬에서는 들여쓰기 없이 선언된 변수가 전역변수로
취급되며 전역변수는 함수 내부, 제어문 내부 등
프로그램 어디에서나 사용이 가능합니다.
'''
sale_rate = 0.8 # 전역 변수.

def calc_price(price):
    print("오늘의 할인율: ", sale_rate)
    
    today_price = price * sale_rate #지역 변수.
    print("오늘의 가격:",today_price)
    print("-" * 40)

# print(today_price)
print(sale_rate)
calc_price(1000)

sale_rate = 0.7
calc_price(1000)
print(sale_rate)

print("-" * 40)

money = 1000 # 전역 변수.

# 메모리 주소값을 확인하는 함수 id()
def discount():
    print("discount 함수가 실행됨!")
    global money # 함수 내부에서 전역변수를 사용하겠다.
    money = 500 # 지역변수
    
    print("지역변수 money의 값: ",money)
    print("지역변수 money의 주소값: ",id(money))

discount()
print("지역변수 money의 값: ",money)
print("지역변수 money의 주소값: ",id(money))

















