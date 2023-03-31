
'''
* 구구단 n단 출력하기
1. 구구단 n단을 wihle문을 사용하여 출력하세요.
2. 구구단 단수는 사용자에게 입력받아서 출력하세요.

ex) 구구단을 입력하세요: 4

*** 구구단 4단 ***
4 x 1 = 4
4 x 2 = 8
4 X 3 = 12
4 X 4 = 16
.
.
.
4 x 9 = 36

'''

dan = int(input("구구단을 입력하세요: "))
hang = 1

print("*** 구구단 ", dan, "단***")
print("=" * 40)

while hang <= 9:
    print(dan, "x", hang, "=", dan * hang) 
    hang += 1
    




