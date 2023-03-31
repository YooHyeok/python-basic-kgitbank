'''
* 문자열 알파벳 형태 변경 메서드

1. lower(): 영문 알파벳을 모두 소문자로 변환.
2. upper(): 영문 알파벳을 모두 대문자로 변환.
3. swapcase(): 영문 대소문자를 각각 반대로 뒤집음.
4. capitalize(): 문장의 맨 첫글자만 대문자로, 나머지는
소문자로 변환.
5. title(): 각 단어의 맨 첫글자만 대문자로, 나머지는
소문자로 변환.
'''
s = "Good AFTerNoOn!!! my nAme is YOo"
print(s)
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 사용자에게 '사과'의 영문 철자를 입력받아서
# 사용자가 대문자로 입력하든, 소문자로 입력하든지간에
# apple이라고 작성하면 정답이라고 출력해 보세요.

a = input("사과를 영문 철자를 쓰세요: ")
if a.lower() == "apple":
    print("정답입니다!")
else:
    print("오답입니다~")































































