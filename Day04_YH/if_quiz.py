
'''
1. 국, 영, 수 평균점수가
 60점 이상이라면
 "이번 시험에 통과하셨습니다" 를 출력하세요.
  
2. 60점 미만이라면
 "재수강 대상자 입니다." 를 출력하세요.
 
3. 조건에 관계없이
 "열공하세요!"를 출력하세요.
'''

k = int(input("국어점수: "))
e = int(input("영어점수: "))
m = int(input("수학점수: "))

tot = k + e + m
avg = round(tot / 3, 2)

print("당신의 평균점수 : ", avg, "점")
if avg >= 60:
    print("이번시험에 통과하셨습니다.")
if avg <= 60:
    print("재수강 대상자 입니다.")  
print("열공하세요!")






