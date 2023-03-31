
'''
* 식별자 (identifier)

1. 식별자는 사용자 정의로 데이터에 이름을 붙여놓은 것을 말합니다.
2. 모듈, 패키지, 변수 , 함수, 클래스 등의 이름을 식별자 라고 합니다.
3. 식별자 이름은 중복해서 지정할 수 없습니다
'''

hong = "홍길동"
shin = "신사임당"
print(hong)
print(shin)

# 식별자 이름을 숫자로 지정하거나 숫자로 지정하면 안됩니다.
# 7 = 777 리터럴(상수)는 식별자 이름으로 인식되지 않습니다.

number7 = 7
num7ber = 7
# 7number = 7 (X) 식별자 앞에 상수가 들어가면 유효하지 않다.

# 대 / 소문자를 다르게 쓰면 다른 식별자로 인식합니다.
banana = "바나나"
Banana = "빠나나"
BaNaNa = "버네이너"

print(banana)
print(Banana)
print(BaNaNa)

# 식별자 이름에는 공백을 포함할 수 없습니다.
# user birth day = 19921023 (X)
userbirthday = 19921023
# 가독성
user_birth_day = 19921023 
# user_birth_day = 19921023 * Python style
userBirthDay = 19921023
# userBirthDay = 19921023 * Java style

# if, while과 같은 이미 기능이 내포되어 있는 키워드 (예약어)
# 는 식별자 이름으로 사용할 수 없습니다.
# if = "만약에" (X)
IF = "만약에"

# print()와 같은 내장함수의 이름은 식별자 이름으로
# 사용할 수는 있지만, 더이상 함수의 기능을 사용할 수 없습니다.

# print = "출력하다." (X)
Print = "출력하다"
print(Print)

#한글, 한자 등 영어 이외의 문자도 식별자 이름으로 사용이 가능합니다.
名 = "홍길동"
야옹이 = "고양이"
print(名)
print(야옹이)

# sagwa = "사과"






























