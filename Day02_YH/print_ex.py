
'''
* 표준 출력함수 print()

- 파이썬의 표준 출력함수 print는 괄호 안에 출력하고 싶은
변수, 리터럴 상수, 수식 등을 적으면 콘솔창에 텍스트 출력을
실행합니다.
'''

value = 1234
name = "홍길동"
print(value)
print(name)
print(5678)
print("홍길동")
print(value * 3)

'''
- 출력할 데이터가 여러 개라면 괄호 안에 출력할 데이터들을
콤마(,)로 나열하여 작성합니다.
- 이 때 여러 개의 값들을 공백과 함께 가로로 나란히 출력합니다.
'''
dog = "멍멍이"
cat = "야옹이"
print(dog, cat, name, "좋아요")

'''
- print함수 내부에는 sep이라는 속성이 존재합니다.
- sep은 separator의 약자로 구분자라고도 부릅니다.
- sep 속성의 기본값은 " " 공백 문자열이 지정되어 있으며,
만약 변경하고 싶다면 sep속성을 직접 작성하여 변경합니다.
'''
print("--------------------------")
print(dog, cat, "좋아요~", sep=" ")
print(dog, cat, "좋아요~", sep=", ")
# 멍멍이=>야옹이=>좋아요~
print(dog, cat, "좋아요~", sep="=>")

print("-------------------------------")

# sep 속성을 이용하여 '닭강정 먹고 김말이 먹고 볶음밥 먹고 짜장면'
# 이 문장을 하나의 print()함수로 출력하세요.

Food1 = "닭강정"
Food2 = "김말이"
Food3 = "볶음밥"
Food4 = "짜장면"
print(Food1, Food2, Food3, Food4, sep=" 먹고 ")

print("-------------------------------")
'''
- end속성은 데이터 출력 이후 맨 끝에 포함할 문자를
 지정하는 용도입니다.

-파이썬의 print함수가 자동으로 줄 개행을 하는 이유는
 print함수 내부에 end라는속성값이 지정되어 있고, 기본값으로
 탈출문자 ("\n": 줄 개행명령)이 포함되어 있기 때문입니다.
 '''


print(dog, cat, end=" ")
print(dog, end="\n")
print(cat)

# 멍멍이와 야옹이 신난다!!!


print(dog, end="와 ")
print(cat, end=" ")
print("신난다!!!")

print("안녕", "잘가", end="요!\n", sep="!!")

print(dog)
print(cat)








































