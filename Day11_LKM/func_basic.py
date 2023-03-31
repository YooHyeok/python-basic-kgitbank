
sum = 0
for n in range(1, 6):
    sum += n
print("1~5까지의 누적합:",sum)

###############################

sum = 0
for n in range(1, 11):
    sum += n
print("1~10까지의 누적합:", sum)

###############################

sum = 0
for n in range(1, 101):
    sum += n
print("1~100까지의 누적합:", sum)

'''
* 함수 (Function)

- 함수는 지속적으로 사용되는 코드블록에 이름을 붙여놓은
 형태입니다.
 
- 함수는 한 번 정의해 두면 지정해둔 함수 이름을 통해
 언제든지 해당 코드 블록을 재사용할 수 있습니다.
 
- 함수를 정의할 때는 def라는 키워드를 사용합니다.

- 정의해 놓은 함수를 사용하는 것을 호출(call)이라고 부릅니다.

- 파이썬에서는 함수를 호출하려면 반드시 호출문보다 상단부에
 함수를 먼저 정의해야 합니다.
'''

# 함수의 정의. (1~x까지의 누적합을 구하는 함수)
def calc_sum(x):
    print("calc_sum함수가 호출됨!")
    sum = 0
    for n in range(1, x+1):
        sum += n
    return sum

print("-" * 40)

# 함수의 호출.
print("1~5까지의 누적합:", calc_sum(5))
print("1~10까지의 누적합:", calc_sum(10))
print("1~100까지의 누적합:", calc_sum(100))

num = calc_sum(100)
# num = 5050
print(num)
print(type(num))
print(type(calc_sum(10)))














