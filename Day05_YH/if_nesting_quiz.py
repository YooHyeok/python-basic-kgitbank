
'''
1. 점수(point)를 입력받아 90점 이상이면
 다시 한 번 조건을 검사해서
 100점을 초과한 경우 "점수를 잘못 입력하셨습니다." 를 출력.
 95 ~ 100점일 때는 "당신의 학점은 A+입니다."
위 두 조건을 모두 만족하지 못하면 "당신의 학점은 A입니다."

2. 다중 분기 조건문을 사용하여 
80점대는 B, 70점대는 C, 60점대는 D, 
그 아래의 점수는 모두 F처리 하세요
'''

point = int(input("점수를 입력하세요: "))

if point >=90:
    if point > 100:
        print("점수를 잘못 입력하셨습니다.")
    elif 100 >= point >= 95:
        print("당신의 학점은 A+입니다.")
    else:
        print("당신의 학점은 A입니다.")
elif 90 > point >= 80:
    print("B")
elif 80 > point >= 70:
    print("C")
elif 70 > point >= 60:
    print("D")
else:
    print("F")
    


if point >=90:
    if point > 100:
        print("점수를 잘못 입력하셨습니다.")
    elif 100 >= point >= 95:
        print("당신의 학점은 A+입니다.")
    else:
        print("당신의 학점은 A입니다.")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
elif point >= 60:
    print("D")
else:
    print("F")




