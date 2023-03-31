
'''
* 문자열 대체 메서드 replace()
- 특정 단어를 모두 찾아서 새로운 단어로 일괄 대체하는 메서드 입니다.
'''
s1 = "파이썬 프로그래밍!!! 파이썬은 문자열을 관리하는\
수많은 메서드 들을 제공합니다!!! 파이썬 짱짱!!!"
print(s1)
print(s1.replace("파이썬","python"))
# print(s1.replace("old","Python"))
s1 = s1.replace("파이썬","python")
print(s1)

print(s1.replace("!",""))

s2 = "아침부터 커피를 마셨는데 점심먹고 커피를 또 마셨어\
... 그런데 저녁에 또 나한테 커피를 주면 오늘 커피를 몇잔 마신거지?"
print(s2.replace("커피","우유", 2))



























