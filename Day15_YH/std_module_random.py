
'''
* 표준 모듈 random

- 프로그램이 무작위 동작을 하게 하려면 난수값(랜덤값)이 필요합니다.

-랜덤값을 난수라고 부르며 난수를 쉽게 발생시킬 수 있는
함수를 제공하는 모듈이 random모듈입니다.

- random모듈의 random()함수는 0.0이상 1.0미만의
실수 난수값을 발생시킵니다.
'''
import random as r

rn = r.random()
# print("랜덤값: ",rn)
print("오늘 저녁은 뭘먹을까요???")

if rn > 0.8:
    print("치킨에 맥주~~~")
elif rn > 0.6:
    print("삼겹살에 소주~~")
elif rn > 0.4:
    print("햄버거나 먹자~~")
elif rn > 0.2:
    print("라면이나 먹자~~~")
else:
    print("굶어!")


'''
- 정수 난수는 randint()함수를 사용합니다.
- randint()는 인수로 시작범위와 끝범위를 지정하는데,
끝범위도 난수값에 포함되는 특징이 있습니다.

 ex) randint(1, 10) -> 1~10까지의 정수 난수 발생.
'''

pets = ['멍멍이', '야옹이', '코끼리', '호랑이', '비둘기']

idx = r.randint(0, 4)
print("애완동물을 뭘 키울까??: ",pets[idx])

'''
- choice함수는 리스트 내부의 임의의 요소를 랜덤으로
선택하여 리턴합니다.
'''
print("-" * 40)
burger = ['맥도날드','버거킹','파파이스','KFC']
print(r.choice(burger))


print("로또 번호 추첨기")
number = range(1, 45)
print("추첨된 번호: ",r.choice(number))

'''
shuffle함수는 리스트의 요소를 무작위로 섞습니다.
'''
print("-" * 40)
print(burger)
r.shuffle(burger)
print(burger)

'''
- sample함수는 리스트의 항목 중 n개를 무작위로 추출하여
새로운 리스트를 만들어 리턴합니다.

-중복값은 자동으로 배제시키며 원본 리스트는 변하지 않습니다.
'''
print("-" * 40)

sample_list = r.sample(burger, 2)
print(sample_list)
print(burger)









