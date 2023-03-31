

import random as r


# 당첨번호 생성
lotto_nums = range(1, 46)
win = r.sample(lotto_nums, 6)
win.sort()

paper = 0 # 로또를 현재 몇 장 구매했는지를 저장할 변수

while True:
    my_lotto = r.sample(lotto_nums, 6)
    my_lotto.sort()
    paper += 1
    
    if win == my_lotto:
        print("1등에 %d번만에 당첨되셨습니다!!!" % paper)
        print("당첨까지 사용한 금액: %d원" % (paper * 1000))
        print("1등 당첨 확률: %.8f%%" % ((1/paper) * 100))
        break
    else:
        print("로또 %d장째 구매중..." % paper)























