
'''
* 반복문 중첩 (loop nesting)

- 외부 반복문 안에 내부 반복문이 존재하는 형태를 반복문 중첩 이라고 합니다.
- 내부 반복문이 종료가 되어도 외부 반복문이 끝나지 않는다면
내부 반복문은 외부 반복문의 제어변수의 크기 및 범위까지 계속
반복실행되게 됩니다.
'''

for dan in range(2, 10):
    print("# 구구단", dan, "단")
    print("=" * 40)
    
    for hang in range(1, 10):
        print(dan,"x",hang,"=",dan*hang)
    print("=" * 40)



