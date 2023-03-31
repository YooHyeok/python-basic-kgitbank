
'''
* 반환값(return value)

- 반환값이란 함수를 호출한 곳으로 함수의 최종 실행 결과를
전달하는 값입니다.

- 인수는 호출부에서 함수로 전달되는 값이고 반환값은
호출부에게 실행결과를 보고하는 값입니다.

- 인수는 여러 개 존재할 수 있지만 반환값은 언제나
하나만 존재해야 합니다.
'''
def add(n1, n2):
    return n1 + n2

result = add(10, 5) # result = 15
print(result)
print("-" * 40)

print(add(17, 3), add(9, 8)) # print(20, 17)

result = add(add(5, 7), add(9, 8)) # add(12, 17) # result = 29
print(result)

# n = int(input("정수: ")) # --> n = int("3")

'''
- 함수의 반환값은 언제나 하나여야만 합니다.
- 단, 복수의 데이터를 반환할 때는 컬렉션 자료형을
사용하여 리턴합니다. (list, tuple, dict, set ....)
'''
def operate_all(n1, n2):
    return n1+n2, n1-n2, n1*n2, n1/n2

result = operate_all(10, 5)
print(type(result))

print("덧셈 결과:", result[0])
print("뺄셈 결과:", result[1])
print("곱셈 결과:", result[2])
print("나눗셈 결과:", result[3])

'''
- 모든 함수가 반환값이 반드시 필요한 것은 아닙니다.
- 함수 실행 후에 딱히 반환할 데이터가 없으면
return을 생략할 수 있습니다.
'''

def bad_words():
    print("메롱메롱~~~~~")
    print("약오르지~~~~~")
    print("때려봐떄려봐~~~~~!")
    
bad_words()
bad_words()
bad_words()
bad_words()

print("-" * 40)
# return이 없는 함수, 참조할값이 없음.
def multi(n1, n2):
    result = n1 * n2
    print("%d x %d = %d" % (n1, n2, result))
    # return result 삽입
a = multi(9, 3)
print("a의 값은:", a) # 결과값 = None # return result 삽입

'''
- 반환값이 없는 함수는 동작만 처리할 뿐 값이 호출부로 돌아오지 
않기 때문에 다른 변수에 대입하거나 수식내에서 사용할수 없고
단독으로 호출하여 사용합니다.
'''

print("-" * 40)
multi(add(2,4),add(4,6)) # multi(6, 10)
# add(multi(2, 2), multi(4, 4)) #멀티 함수에는 return값이 없어서 처리안됨

'''
-모든 함수는 함수 정의부에서 return 키워드를 만나는 순간
함수가 강제로 종료됩니다.

-마치 반복문이 break를 만나면 강제로 종료되는 것과 비슷한 
원리입니다.
'''

print("-" * 40)

def sum_sub(n1, n2):
    return n1 + n2
    return n1 - n2

def sum_mul(n1, n2):
    if n1 > n2:
        return n1 + n2
    else:
        return n1 * n2

print(sum_sub(10, 5))
print(sum_mul(20, 10))
print(sum_mul(10, 20))

def divide(n1, n2):
    if n2 == 0:
        print("0으로 나누지 마세요!!!")
        return
    result = n1 / n2
    print("%d / %d = %d" % (n1, n2, result))
divide(20, 0)

print("-" * 40)

def say_nickname(nick):
    if nick == "빡빡이":
        print("그런 별명 부르지 마세요!!!!")
        return
    print("내 별명은 %s 입니다." % nick)
    
n = input("별명: ")
say_nickname(n)




















