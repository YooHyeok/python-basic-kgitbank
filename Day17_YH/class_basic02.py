

class Calculator:
    
    result = 0 # 계산기의 결과값을 담아줄 변수.
    
    def add(self, n):
        self.result += n
        
    def sub(self, n): # self = 객체에 주소값을 대입
        self.result -= n

# 계산기 객체 생성

cal1 = Calculator() # 1번 계산기 생성.
cal2 = Calculator() # 1번 계산기 생성.
cal3 = Calculator() # 1번 계산기 생성.
cal4 = Calculator() # 1번 계산기 생성.

# 1번 계산기로 계산 수행

cal1.add(17)
cal1.add(13)
cal1.sub(5)

# 2번 계산기로 계산 수행
cal2.add(23578)

# 3번 계산기로 계산 수행

cal3.add(30)
cal3.sub(17)

print("1번 계산기 계산 결과: %d" % cal1.result)
print("2번 계산기 계산 결과: %d" % cal2.result)
print("3번 계산기 계산 결과: %d" % cal3.result)
print("4번 계산기 계산 결과: %d" % cal4.result)