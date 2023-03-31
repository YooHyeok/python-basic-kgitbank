
'''
* UP & DOWN 게임

1. 1~100사이의 정수 난수를 발생시켜서 해당 값을 사용자가 맞추게 
하는 게임입니다.
2. 사용자가 입력한 값이 정답값보다 큰지 작은지 사용자에게 알려주어
사용자가 지속해서 범위를 좁혀가며 답을 찾을 수 있도록 합니다.
3. 정답을 맞췄을 때 프로그램이 종료되도록 프로그램을 구성해 보세요.

4. 사용자가 정답을 맞췄을 때 몇 번만에 정답을 맞췄는지 출력하는
로직을 추가하세요!
'''
# import random as r
# 
# num = r.randint(1, 100)
# n = int(input("숫자를 입력하세요: "))
# cnt = 0
# for n in num:
#     if n == num:
#         break 
#         print("정답입니다!! %d번만에 맞췄습니다." % cnt)   
#     elif n < num:
#         print("UP!!")
#     else:
#         print("DOWN!!")
#         cnt += 1


import random as r

secret = r.randint(1, 100)
count = 0 # 몇번 만에 정답을 맞추었는지를 파악할 변수.
count_down = 0 # 정답 기회가 몇번 남았는지를 파악할 변수

print("[UP & DOWN 게임 - 1~100사이의 숫자 중 어떤 숫자가 들어있을까요????]")

while True:
    print("-" * 40)
    num = int(input("숫자를 입력하세요: "))
    count += 1
    count_down -= 1
    
    if num == secret:
        print("정답입니다!!! %d번만에 맞추셨네요~" % count)
        if count < 8:
            print("이겼습니다~")
        else:
            print("졌습니다! 원샷하세요~")
        break
    elif num < secret:
        print("UP!!!")
    else:
        print("DOWN!!")
    
        if count_down > 0:
            print("정답 기회 %d번 남음!" % count_down)
        else:
            print("정답 기회 모두 소진! 계속 문제를 풀어주세요.")


















