
'''
* 표준 모듈 time

- time 모듈은 시간 관련 기능들을 제공합니다.

- 대표적인 함수는 time()인데 이 함수는 현재 시간을
1970년 1월 1일 자정을 기준으로 현재까지 경과한
시간을 초단위로 표현한 유닉스 시간을 반환합니다.
'''
import time 
print(time.time())

# time함수를 이용한 프로그램 속도 테스트

start = time.time()

sum = 0
for n in range(500000):
    sum += n
    
end = time.time()
print("프로그램 실행속도: %.8f초" % (end - start))

'''
- time 모듈의 sleep()함수는 cpu를 지정한 시간만큼
잠재워 아무것도 하지 않고 시간을 끌게 합니다.

- 인수값에 초단위 시간을 전달합니다.
'''
'''
print("-" * 40)

print("재밌는 문제를 준비했어용~~")
time.sleep(3)
print("대학생이 힘이 센 이유는??")
time.sleep(10)
print("개강하니까~~~~~")
time.sleep(3)
print("흐으엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
'''

'''
* 연습- 전체 구구단을 2단부터 9단까지 출력하는데,
단의 행 출력 간격은 0.2초, 단이 바뀔떄는 1초를 쉬었다가
출력하도록 sleep()을 사용하여 구성해 보세요.
'''
for dan in range(2, 10):
    print("# 구구단", dan, "단")
    time.sleep(1)
    print("=" * 40)
    
    for hang in range(1, 10):
        time.sleep(0.2)
        print(dan,"x",hang,"=",dan*hang)
    print("=" * 40)




















