
# 1번 계산기의 결과값을 저장할 변수
result1 = 0

# 더하기 기능을 실행할 함수.
def add(n): # n은 더할값을 전달받는 인수.
    global result1
    result1 += n
    
# 빼기 기능을 실행할 함수.
def sub(n):
    global result1
    result1 -= n 
    
# 2번 계산기의 값을 저장할 변수
result2 = 0

# 더하기 기능을 수행할 함수
def add2(n):   
    global result2
    result2 += n

# 빼기 기능을 수행할 함수
def sub2(n):
    global result2
    result2 -= n

add(5)
add(12)
sub(5)
add(20)
add(3)
sub(14)

add2(3)
add2(13)
sub2(4)

print("1번 계산기의 결과: %d" % result1)
print("2번 계산기의 결과: %d" % result2)














































