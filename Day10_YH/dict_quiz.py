
'''
1. eng_kor이라는 이름으로 빈 사전을 하나 만드세요.

2. 사용자가 '그만'을 입력할 때까지 영단어를 입력받습니다.

3. 총 두번을 입력받으시는데, 영단어를 key값으로, 한글 뜻을 value값으로
지정하여 사전(dict)에 등록하세요.

4.'그만'을 입력하여 단어장 만들기를 종료하면,
그동안 입력받았던 사전의 내부 데이터를 출력하세요.
'''

eng_kor = {}
print("[영어 단어장 만들기]")
print("- 종료하시려면 영단어 입력창에 '그만'을 입력하세요.")

while True:
    eng = input("영단어: ")
    if eng == "그만":
        break
        print("종료합니다.")
    elif eng in eng_kor:
        print("이미 등록된 단어입니다.")
        continue
    else:
        kor = input("뜻: ")
        eng_kor[eng] = kor
        
    print("\n*** 단어장***")
    print("-" * 40)
    for k in eng_kor:
        print(k,":",eng_kor[k])
    print("-" * 40)

print("\n*** 오늘 공부한 단어***")
print("-" * 40)
for k in eng_kor:
    print(k,":",eng_kor[k])
print("-" * 40)    
    
    
    
