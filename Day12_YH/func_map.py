
'''
* 내장함수 map

- map()은 첫번째 인수로 자료형을 저장하고, 두번째 인수로
여러 값의 집합형(list, tuple, dict...)를 지정하면
해당 집합형 내부 요소값을 일괄적으로 첫번째 인수로
지정한 타입으로 변경한 데이터를 반환합니다.
'''

# 3개의 숫자 중 최대값을 판별하여 리턴하는 함수를 정의하세요.

# def max_of_three(n1, n2, n3):
#     if n1 > n2 and n1 > n3:
#         print("%d 이 최대값 입니다" % n1)
#         return
#     elif n2 > n1 and n2 > n3:
#         print("%d 이 최대값 입니다" % n2)
#         return 
#     elif n3 > n1 and n3 > n2:
#         print("%d 이 최대값 입니다" % n2)
#         return
#     elif n1 == n2 and n1 == n3
#         print("세 숫자 값이 모두같습니다")
#         return

def max_of_three(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    else:
        if n2 > n3:
            return n2
        else:
            return n3
# -        
# n1, n2, n3 = input("값 3개 입력: ").split() # 공백을 기준으로 입력한다
# print(n1, n2, n3)
# print("%s, %s, %s중에 최대값: %s" 
#        % (n1, n2, n3, max_of_three(n1, n2, n3)))

n1, n2, n3 = map(int,input("값 3개 입력: ").split())
print(n1, n2, n3)
print("%d, %d, %d중에 최대값: %d" 
       % (n1, n2, n3, max_of_three(n1, n2, n3)))
# -
# n1 = int(input("n1: "))
# n2 = int(input("n2: "))
# n3 = int(input("n3: "))
# print("%d, %d, %d중에 최대값: %d " 
#       % (n1, n2, n3, max_of_three(n1, n2, n3)))
















