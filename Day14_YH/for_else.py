

# for ~ else문을 이용한 범위 안의 모든 소수를 출력하기.

n1, n2 = map (int, input("정수 2개를 입력하세요: ").split())

if n1 > n2:
    n1, n2 = n2, n1

'''
* for ~ else

- for ~ else구문은 for문 내부에서 break를 한번도 만나지
않고 반복문이 끝까지 정상 수행되었을 경우 for문이 가지고 있는
 else문의 코드가 실행되는 구조입니다.
 
- 반복 도중에 break를 만나서 for문이 강제로 종료되면
 for문의 else는 실행되지 않습니다.
'''    
cnt = 0 # 소수의 갯수를 저장할 변수.

for i in range(n1, n2+1): # 10, 30
    for j in range(2, i):
        # 정수를 2부터 해당 정수까지 나누었을 때
        # 도중에 나누어 떨어진다면 소수가 아니므로
        # break를 사용하여 반복문을 탈출합니다.
        if i % j == 0: 
            break
        
    else: # for문에서 break가 한번도 작동하지 않았을 경우 실행.
        print("%d" % i, end=" ")
        cnt += 1
        if cnt % 8 == 0:
            print()
        
print()
print("-" * 40)
print("총 소수의 갯수: %d개" % cnt)





















