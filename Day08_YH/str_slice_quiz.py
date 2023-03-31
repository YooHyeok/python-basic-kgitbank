'''
주민등록번호를 입력하세요:
주민등록번호 앞자리:
주민등록번호 뒷자리:
1995년도 2월 11일 25세 남자
'''

x = input("주민등록번호를 입력하세요: ")
int = x #int(x)
print("주민등록번호 앞자리:",x[:6:1])
print("주민등록번호 뒷자리:",x[7:14:1])
y = x[:2]
m = x[2:4]
d = x[4:6]
gender = x[7]

if(gender == 1) or (gender == 2):
    gender = "남자"
elif(gender == 3) or (gender == 4):
    gender = "여자"
    






