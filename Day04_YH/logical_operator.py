
'''
* 논리 연산자 (&, |, and, or, not)

- 양쪽 항의 논리값의 연산을 수행하는 연산자 입니다.

# &, and 연산자는 좌항과 우항과의 논리값이 모두 True 일
경우에만 전체 결과를 True로 도출합니다.
'''
a = 3

if a > 1 and a < 10:
    print("a는 1보다 크고 10보다는 작습니다.")
else:
    print("a는 1 ~ 10사이의 숫자가 아닙니다.")
    
# 파이썬은 위의 식을 연결해서 표현할 수 있습니다.
if 1 < a < 10:
    print("ok!")
    
'''
# |, or 연산자는 좌항과 우항의 논리값이 한쪽만 True여도
전체 결과를 True로 도출합니다.
'''
b = 4

if b == 2 or b == 4:
    print("b는 2 또는 4입니다.")
else:
    print("b는 2나 4가 아닙니다.")

'''
* 단축평가(short circuit: and, or)

- 논리 연산 수행시 좌항에서 전체 결과가 판명날 경우
우항 연산을 진행하지 않는 연산자 입니다.
'''
print("_" * 40)
c = 0
    
if (c == 0) or (10 /c ==5):
    print("에러없이 통과!!!")

# not 연산자는 논리값을 반전시킵니다. (True->False, False->True)
print("_" * 40)

d = 10

if not d < 0:
    print("d는 0보다 작지않습니다.")
    
if not d == 0:
    print("d는 0이 아닙니다.")
    
'''
- C언어에서는 정수 0을 False로 해석하고, 0이 아닌
모든 정수를 True로 해석합니다. 파이썬도 C의 논리해석을
 그대로 적용할 수 있습니다.
'''
    
apple = 0
if apple:
    print("사과가", apple, "개 있습니다.")
else:
    print("사과가 하나도 없습니다.")
    
    
    
    
    
    
    
    
    
    
    






