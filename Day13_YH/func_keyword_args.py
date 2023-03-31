
'''
* 키워드 인수 (keyword argument)

- 인수의 갯수가 많아지면 인수의 순서를 잘 파악하기 어렵고
 함수를 호출할 때 전달할 값의 위치를 헷갈릴 가능성이
 높아집니다.

ex) def signup_user(id, pw, name, addr, phone, gender .....)

- 파이썬에서는 순서와 무관하게 인수를 전달할 수 있는
방법을 제공하여 인수의 이름을 직접 지정하여 값을 전달하는
키워드 인수 방식을 허용합니다.
'''

def calc_stepsum(begin, end, step):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

# print(calc_stepsum(begin=3, 7, 1))
# print(calc_stepsum(end=3, 7, 1))

# 위치 인수값을 사용.
print(calc_stepsum(3, 7, 1))

# 키워드 인수값을 사용.
print(calc_stepsum(begin=3, step=1, end=7))
print(calc_stepsum(end=7, step=1, begin=3))

# 위치 인수와 키워드 인수의 혼합 사용.
print(calc_stepsum(3, step=1, end=7))
# print(calc_stepsum(end=7, 3, 1)) (x)
print(calc_stepsum(begin=3, end=7 ,step=1))

print(3, 6, 9, end="\n", sep=" ")
print()
print(3, 6, 9, sep="**", end="=>")
print()
print(3, 6, 9, end="=>", sep="**")
print()











