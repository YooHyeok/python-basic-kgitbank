
'''
* 인수(arguments)

- 인수는 함수를 호출할 때 함수 실행에 필요한 값들을 전달하는
매개체 역할을 하며, 그렇기 때문에 매개변수(parameter)라고도
 부릅니다.

- 함수 호출부에서 어떤 인수값을 전달하느냐에 따라 함수의
실행결과가 달라집니다.
 
- 인수의 갯수는 제한이 없어 많은 값을 함수에 전달할 수 있고
하나도 전달하지 않을 수도 있습니다.

- 함수를 정의할 때 지정한 인수의 갯수만큼 호출할 때도
동일한 수의 인수값을 전달해야 합니다.

- 인수의 이름을 지어 줄 때는 아무렇게나 지어도 무방하지만
이 함수를 처음 사용하는 사람도 인수 이름만 보고 무슨 값을
전달해야 할지 의미를 알기 쉽게 지정하는 것이 좋습니다.
'''

def get_items(weapon, armor):
    w = "'%s' 무기를 획득했습니다." % weapon
    ar = "'%s' 방어구를 획득했습니다." % armor
    detail = w + "\n" + ar + "\n--------------------"
    return detail

print(get_items("대검", "철갑옷"))
print(get_items("천갑옷", "목검"))

# 인수를 전달받지 않는 함수의 예.
def get_board_article():
    return '게시글을 30개 가져왔습니다.'
print(get_board_article())
print(get_board_article())
print(get_board_article())
print(get_board_article())


'''
* 연습
1. 인수를 정수형태로 시작값(start), 끝값(end)을 입력받아
반복문으로 start부터 end까지의 누적 총합을 구하는 함수를 정의하세요.

2. 함수 이름은 calc_rangesum으로 정의하세요.
ex calc_rangesum(3, 7) ==> 3부터 7까지의 누적합을 구해와야 함.

3. 출력예시: "x ~ y 까지의 누적합: z"
'''

x = int(input("start: "))
y = int(input("end: "))
def calc_rangesum(x, y):
    sum = 0
    for n in range(x, y + 1):
        sum += n
    return sum

print("%d ~ %d까지의 누적합: %d" % (x, y, calc_rangesum(x, y)))










