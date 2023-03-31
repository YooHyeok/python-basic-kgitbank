

'''
* if ~ else

- if블록이 조건식의 결과가 True일 경우에만 실행된다면
else블록은 위의 if의 결과가 false일 경우에만 실행됩니다.

- if문 뒤에는 반드시 논리값을 반환하는 조건식을 적어야 하지만
else문 뒤에는 아무것도 적지 않습니다.

-if문은 단독 사용이 가능하지만 else는 반드시 if와 함께
사용해야 합니다.
'''
money = int(input("현재 갖고있는 금액: "))

if money >= 20000:
    print("치킨 시켜먹자~")
else: 
    print("그냥 라면이나 먹자ㅠㅠ")
    
print("_" * 40)

password = input("비밀번호를 입력하세요: ")
if password == "abc1234!":
    print("로그인 되셨습니다.")
else:
    print("비밀번호가 틀렸습니다.")




