
'''
* 문자열 포맷팅

- 포맷팅은 문자열 사이사이에 다른 타입의 데이터를 넣어서
문자열을 조립하는 방식입니다.

- 포맷팅에 사용하는 서식 문자
1. %d: 10진수의 정수
2. %f: 실수
3. %s: 문자열
4. %%: 특수문자 %
'''

bts = 7
print("방탄소년단은", bts,"명 입니다.")
print("방탄소년단은 %d명 입니다." % bts)

'''
- 여러 개의 데이터도 하나의 문자열에 포맷팅할 수 있는데,
이 때는 % 연산자 뒤에 나열할 변수를 ()로 묶어야 합니다.
'''
month = 8
day = 15
anni = "광복절"
print(month, "월", day, "일은", anni, "입니다.")
print("%d월 %d일은 %s입니다." % (month, day, anni))

print("_" * 40)
percent = 40
print("파이썬의 진도율은 %d%%입니다." % percent)
print("-" * 40)

for dan in range(2, 10):
    print("구구단 %d단" % dan)
#    print("# 구구단", dan, "단")
    print("=" * 40)
    
    for hang in range(1, 10):
        print("%d x %d = %d" % (dan, hang, dan*hang))
#         print(dan,"x",hang,"=",dan*hang)
    print("=" * 40)


'''
* 실수 포맷팅 서식문자 %f

- %f는 기본적으로 소수점 6자리를 표현하도록
설정되어 있습니다.

-만약 자리수를 조절하고 싶다면 %.자리수f를 사용합니다.
'''
pi = 3.1415926535897

print("원주율의 값은 %f입니다." % pi)
print("원주율의 값은 %.2f입니다." % pi)
print("원주율의 값은 %.5f입니다." % pi)
print("원주율의 값은 %.14f입니다." % pi)

print("1인치는 %fcm입니다." % pi)
print("1인치는 %.2fcm입니다." % pi)
print("1인치는 %.0fcm입니다." % pi)

'''
* 문자열 포맷팅 폭 지정하기

- 포맷팅 출력 방식을 사용하면 포맷 문자열이 차지할 공간의
길이를 지정할 수 있습니다.

- 폭 지정을 하면 문자열을 정돈된 형태로 출력할 수 있습니다.

- 포맷팅 서식문자 자리에 양수값을 주면 해당 숫자만큼
자리를 차지하며 우측 정렬합니다. 음수값을 주면 
좌측 정렬 합니다.
'''
print("-" * 40)

p = "파이썬 프로그래밍"
print("%5s" % p)
print("%10s" % p)
print("%20s" % p)
print("%30s" % p)

a = 1234
print("~~~~%5d~~~~" % a)
print("~~~~%-5d~~~~" % a)
print("~~~~%10d~~~~" % a)





































