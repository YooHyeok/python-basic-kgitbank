
'''
* 연습 - 컬렉션(리스트, 튜플, 집합)에 로또 번호를 6개를 랜덤으로 담아서
오름차순으로 출력하세요.
단, 중복숫자는 배제하세요.
'''

import random as r
import time
# 1번째 방법
'''
lotto = []
while len(lotto) < 6:
    num = r.randint(1, 45) # 1부터 45까지의 난수 발생.
    if num not in lotto:
        lotto.append(num)
lotto.sort()
'''
# 2번째방법
'''
lotto = set()
while len(lotto) < 6:
    num = r.randint(1, 45)
    lotto.add(num)
lotto = list(lotto)
lotto.sort()
'''
# * 3번째방법
lotto_nums = range(1, 46)
lotto = r.sample(lotto_nums,6)
lotto.sort()

print("오늘은 이번호로 사야지~")
print(lotto)


win = [] # 당첨번호
while len(win) < 6:
    num = r.randint(1, 45) # 1부터 45까지의 난수 발생.
    if num not in win:
        win.append(num)
        
win.sort()        
print("로또 당첨번호 추첨을 시작합니다!")
for n in win:
    print(n, end=" ")
    time.sleep(0.5)
print()


# 보너스 번호 생성.
while True:
    num = r.randint(1, 45)
    if num not in win:
        bonus_num = num
        break;
    
print("# 보너스 번호:",bonus_num)

cnt = 0 # 맞춘 번호의 갯수를 저장할 변수.
for n in lotto:
    if n in win:
        cnt += 1
        
if cnt == 6:
    print("1등입니다.")
elif cnt == 5:
    if bonus_num in lotto:
        print("2등입니다.")
    else:
        print("3등입니다.")
elif cnt == 4:
    print("4등입니다.")
elif cnt == 3:
    print("5등입니다.")
else:
    print("꽝~")        
        
        
        
        
        
        
        
        
        
        

# for n in range(0, 6):
#     n = range(1, 46)
#     print("추첨된 번호: ",r.choice(n))
#     
# sample_list = r.sample(n, 6)
# print(sample_list)






























