
'''
* 정수형 (integer)

- 수치형 타입 중에 정수형(int)은 양수, 음수의 정수값을 표현하며,
소수점 이하 자리는 표현할 수 없습니다.

- 다른 언어는 정수의 저장범위가 정해져 있지만, 파이썬은 메모리가 허용하는 대로
무수히 많은 정수값을 저장할 수 있습니다.
'''
num = 1234

# 변수의 자료형을 확인하는 함수 : type()
print(type(num))

num2 = -4321
print(type(num2))

# 2진수, 8진수, 16진수도 저장이 가능합니다.

# 2진수 저장 시에는 리터럴 정수 앞에 접두어 0b를 붙입니다.
a = 0b1011
print(a)

# 8진수 저장시에는 접두어 0o를 붙입니다.
b = 0o77
print(b)

# 16진수 저장시에는 접두어 0x를 붙입니다.
c = 0xAC00
print(c)

# 정수를 다른 진법으로 출력하려면 아래의 함수를 이용하면 됩니다.
print("---------------------------")
print(bin(33)) # 2진수 변환함수 bin()
print(oct(0b111001))
print(hex(8923))