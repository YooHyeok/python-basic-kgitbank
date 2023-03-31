

def calc_sum(end):
    sum = 0
    for n in range(end+1):
        sum += n
    return sum

def info():
    print("모듈 임포트 연습!")

inch = 2.54


'''
* 테스트 코드 작성법

- 처음부터 import를 목적으로 설계된 모듈의 테스트 코드 
작성시에는 다음과 같은 문법 하에서 테스트를 실행합니다.

ex) if __name__ == "__main__":
        test code....
        
- __name__ 변수에는 실행 중인 모듈의 이름이 저장되는데
현재 모듈에서 실행할 때는 "__main__"이 저장됩니다.
'''

print("__name__의 변수의 값:", __name__)

if __name__ == "__main__":
    print("1~100까지의 누적합:", calc_sum(100))
    info()
    print("잘된다 개꿀~~~")









































