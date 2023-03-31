
'''
* 다중 분기 조건문 if ~ elif ~ else

- 조건 선택 분기를 여러 개 설정하고 싶다면
 if 블록 아래에 elif라는 키워드를 쓰고 새로운 조건을
 설정합니다.
 
- 시작 if문의 조건식의 결과가 False일 경우 아래에 있는
 elif문의 조건식을 새롭게 테스트하여 해당 조건이 True일 경우
 elif의 종속된 코드를 실행합니다.
 
- elif문은 여러개 쓰는것도 가능합니다.

- if ~ elif문에서 주의할 사항은 조건식을 위에서부터 차례대로
검사하면서
'''

age = int(input("나이: "))

if age >= 20:
    print("성인입니다.")
elif age >= 17:
    print("고등학생입니다.")
elif age >= 14:
    print("중학생입니다.")
elif age >= 8:
    print("초등학생입니다.")
else:
    print("미취학 아동입니다.")



