
'''
* continue

- break가 반복문 강제로 종료시킨다면, continue는
이번 반복 1회차만 건너 뛰고 다음 반복부터는 정상적으로
실행을 계속하게 하는 탈출문입니다.
'''

for n in range(1, 11):
    if n == 6:
        continue
    print(n, end=" ")
print("\n반복문 종료!")

points = [92,46,22,-13,87,-1,100,34,120]

for p in points:
    if p<0 or p>100:
        continue
    print(p, end=" ")
print("\n점수처리 완료!")

# continue를 사용하여 1~30까지의 정수 중 홀수를 가로로 출력해 보세요.

for n in range(1, 31):
    if n % 2 == 0 :
        continue
    print(n, end=" ")
print()   


while True:
    num = int(input("정수를 입력하세요: "))
    
    if num == 1:
        break
    elif num == 0:
        print("다른 숫자를 입력해 주세요.")
        continue
    print(10 / num)
    









