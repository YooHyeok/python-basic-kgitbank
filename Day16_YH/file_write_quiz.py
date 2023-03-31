
'''
* 사용자의 입력을 파일 (xxx.txt)에 저장하는 프로그램을 작성하세요.
(단, 프로그램을 다시 실행하더라도 파일명이 동일하다면
기존 작성한 내용을 유지하고
새로 입력한 내용이 추가되어야 합니다. 또한 파일명도 입력을 받아서 저장하세요.)

***실행 예제***
출력예시: 저장할 내용을 입력:
실행할 때마다 사용자가 입력한 내용이 xxx.txt파일에 추가되어야 합니다.
'''






print("저장할 내용을 입력('그만' 이라고 입력시 종료됩니다.)")

user_input = "" # 입력할 내용
while True:
    temp = input() + "\n" #한번 입력 받을때마다 줄 개행 실행
    if temp == "그만\n":
        break
    user_input += temp
f_path = r"D:\py1230\%s.txt" % temp
f_name = input("파일명을 입력: ")

try:
    f = open(f_path, "a") # 내용을 추가하기 위해 'a'를 사용
    
    f.write(user_input) #입력한 내용을 줄단위로 구분하기 위해 줄바꿈문자삽입.
    print("파일 저장 성공!")
except:
    print("파일 저장 실패!")
finally:
    f.close()





