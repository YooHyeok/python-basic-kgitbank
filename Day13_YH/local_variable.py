


'''
* 지역변수 (local Varible)

- 지역변수란 함수 내부에 선언된 변수를 말합니다.

- 지역변수는 함수 내부에서만 사용할 수 있으며
 함수의 호출이 종료되는 순간 메모리에서 자동 소멸됩니다.
 
- 지역변수의 사용을 함수 내부로 제한하는 이유는
 변수의 이름 충돌을 피하고 메모리를 절약하기 위함입니다.
'''
def info():
    word = "안녕" # 지역변수
#     print(word)
    return word
# info()
word = info()
print(word)
    
def food():
    name = "육개장" # 지역변수
    print(name)
    
food()
# print(name)


