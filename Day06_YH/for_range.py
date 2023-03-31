
'''
* 내장함수 range()

- 순차적으로 증가하는 정수의 리스트를 만들 때
대괄호 안에 데이터들을 콤마로 일일히 나열하는 것은
한계가 있기 때문에, range함수를 사용하면 보다 쉽게
순차형 리스트를 생성할 수 있습니다.

ex)range(begin, end, step) #초기값, 끝값, 증감값
- begin은 값이 포함되지만 end는 값이 포함되지 않습니다.
  (이상, 미만 개념)
'''
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

list1 = list(range(1,11,1))
print(list1)

# step값 생략 시 1로 자동 처리.
list2 = list(range(4,15))
print(list2)

# range함수 괄호 안에 값을 한개만 주면 end로 처리하고
# begin값을 자동으로 0으로 처리합니다.
list3 = list(range(5)) # range(0, 5, 1)
print(list3)

# 1~100까지의 총합을 구하는 로직.
print("_" * 40)

total = 0 # 누적합을 담아줄 변수.
for n in range(1, 101, 1):
    total += n

print("1~100까지의 총합:", total)

# 7 ~ 200 까지의 정수 중 7의 배수로만 가로로 출력하기 (for).
print("_" * 40)
for n in range (7, 201, 7):
    print(n, end=" ")

print()

# 1~100까지의 정수 중 6의 배수이면서
# 12의 배수가 아닌 수를 모두 가로로 출력하세요.

for n in range(1,101):
    if(n % 6 == 0 and n % 12 != 0):
        print(n, end=" ")
# 1~9876 사이의 정수 중 13의 배수의 갯수를 출력.

print()
count = 0
for n in range(1, 9876):
    if n % 13 == 0:
        count += 1
print(count)

















