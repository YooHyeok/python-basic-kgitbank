
'''
* while 연습
- 정수를 2개 (x, y) 입력받아 x부터 y까지의
누적합계를 while을 사용하여 구하는 코드를 만드세요.
ex) 출력예시: "x부터 y까지의 누적합계: z"
'''


x = int(input("x값 : "))
y = int(input("y값: "))

'''
if x > y:
    t = x
    x = y
    y = t
'''
if x > y:
    x,y = y,x

z = 0
n = x
while n <= y:
    
    z += n
    n += 1

print(x, "부터", y ,"까지의 누적합계: ", z)



