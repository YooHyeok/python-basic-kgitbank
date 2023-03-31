
'''
* 중첩 if문
- 중첩 if문은 if 블록 내부에 새로운 if문이 있는
형태입니다.

-바깥쪽 if문의 조건을 테스트 한 뒤, True가 나올경우
다시 내부의 if문을 검사하는 형태로 단계적 조건 판단을 수행합니다.
'''

height = int(input("키를 입력하세요: "))

if height >= 140:
    age = int(input("나이를 입력하세요: "))
    if age >= 8:
        print("놀이기구를 탑승하실 수 있습니다.")
    elif age >= 6:
        print("보호자 동반 시 탑승하실 수 있습니다.")
    else:
        print("나이가 6세 미만입니다.")
        print("놀이기구를 탑승하실 수 없습니다.")
else:
    print("키가 140cm 미만입니다.")
    print("놀이기구를 탑승하실 수 없습니다.")



print("_" * 40)

i = 7 

while i <= 200:
    if i % 7 == 0:
        print(i, end=" ")

    i += 1