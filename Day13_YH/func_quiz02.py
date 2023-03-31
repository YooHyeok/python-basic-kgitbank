
'''
* n의 약수의 갯수를 구하기

1. 정수 n을 전달받아 n의 약수들을 출력하고
약수의 갯수를 리턴하는 함수 calc_divisor을 정의하세요.

2. 약수의 출력은 함수내부에서 이뤄져야합니다.

3. 힌트) 전달받은 n을 1부터 n까지 지속적으로 나누어서
나누어 떨어졌을 시 약수 갯수를 카운팅하고 출력.
'''

# num = int(input("정수: "))
# n = 1
# def calc_divisor(num):
#     count = 0
#     for n in range(1, num+1): # range(1, 31, 1) [1,2,3,4 ... 30]
#         if num % n == 0:
#             count += 1
#     return count
# print(calc_divisor(num))



# ---------------------------------------------------------------------
num = int(input("정수: "))
def calc_divisor(n):
    count = 0
    print("# %d의 약수: " % n, end=" ")
    for x in range(1, n+1):
        if n % x == 0:
            print(x, end=" ")
            count += 1
    print()
    return count    
         
print("# %d의 약수의 갯수: %d개" % (num, calc_divisor(num)))



def get_max(*nums):
    max = nums[0]
    
    for n in nums:
        if n > max:
            max = n
    return max

# print("최대값: %d" % get_max(10, 35, 23, 66, 44, 22))


n_list = list(map(int, input("정수: ").split())) 
print(get_max(n_list))










