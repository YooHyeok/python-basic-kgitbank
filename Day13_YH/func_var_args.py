
def add(n1, n2):
    return n1 + n2

def add3(n1, n2, n3):
    return n1 + n2 + n3

print(add(10, 2))
print(add3(10, 2, 3))

'''
* 위치 가변인수

- 함수를 호출할 때는 함수를 정의했을 시 지정한 인수의 갯수만큼
 값을 전달해야 합니다.
 
- 하지만 가변인수를 사용하면 하나의 인수로 여러개의 값을
 받아서 처리할 수 있습니다.

- 위치 가변인수는 함수 정의부에서 인수를 선언할 때 
 인수 앞에 *기호를 붙여 선언하면 이런 경우에 여러 개의
 데이터를 튜플로 묶어서 함수 내부로 전달합니다.
'''
def calc_total(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

# li = [1,2,3,4,5,6]
print(calc_total(1,2,3,4,5,6,7,8,9,10,100))



def calc_points(name, *points):
    
    print("%s 학생의 성적 계산..." % name)
    
    total = 0
    for p in points:
        total += p
    return total

print("-" * 40)
result = calc_points("김철수", 97,100,80,100,55)
print(result)

def take_two_tuple(tu1, tu2):
    print(tu1)
    print(tu2)
    
take_two_tuple((1,2,3),(4,5,6,7,8))

'''
* 연습1 - n개의 정수를 전달받아 평균값을 구하여
 리턴하는 함수를 작성하세요. (get_avg)

* 연습2 - n개의 정수를 전달받아 n개의 정수 중 가장 큰 숫자를
 리턴하는 함수를 작성하세요. (get_max)
 
힌트) 최대값을 저장할 변수를 선언하고 튜플의 데이터를 반복해서
 서로 비교한 후 최대값 발견시 변수에 새롭게 저장.
'''
print("-" * 40)

# def get_avg(*n):
#         total = 0
#     for x in n:
#         total += x
#         avg += y
#         count += 1
#         y = count / x
#     return(avg)

def get_avg(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum / len(nums)

# n_list = list(map(int, input("정수: ").split())) 
# <= 리스트가 준비되어 있다면 위치가변인수를 사용하지않고 함수식에 바로 대입한다
tu1 = (1,2,3,4,5,6,7,8,9)
print(get_avg(2,4,6,3,4,6,8))






















