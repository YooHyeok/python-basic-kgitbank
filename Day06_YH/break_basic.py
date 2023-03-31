
'''
* 탈출문 (흐름 제어문) - break, continue, return

- 반복문은 조건을 만족하는 동안 코드를 계속 반복실행하기 때문에
한 번 반복이 시작되면 반복 횟수가 끝날 때까지
멈추지 않고 반복을 실행합니다.

- 하지만 중간에 어떠한 이유로 반복을 중지해야 한다거나
현재 반복을 건너 뛰어야 할 경우 탈출문을 사용합니다.

* break

- break는 현재 반복문을 즉시 종료키고 반복문을 탈출합니다.
- 일반적으로 특정 조건 하에서 반복문을 종료시키기 때문에
if 문과 함께 사용합니다.
'''

for n in range(1, 11): #[1,2,3,4,5,6,7,8,9,10]
    if n == 7:
        break
    print(n, end=" ")
print("\n반복문 종료!")

points = [92,56,77,-33,48]
for p in points:
    if(p < 0) or (p > 100):
        print("\n문제가 발생했습니다!!!!!!!!")
        break
    print(p, end=" ")
print("\n점수 처리 완료!")

