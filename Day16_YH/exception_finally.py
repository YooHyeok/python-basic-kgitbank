

'''
* finally 키워드는 예외 발생 여부와 관계 없이 항상 실행해야
할 코드가 있다면 사용하는 예외처리의 키워드입니다.
'''

pets = ['거북이', '강아지', '고양이']

for x in range(4): # [0,1,2]
    try:
        print(pets[x], "키우고싶다~")
    except:
        print("애완동물의 정보가 없습니다.")
    finally:
        print("항상 출력되는 출력문입니다.")
        print("-" * 40)

print("프로그램 정상 종료!")



























