
'''
* 사전 내부 데이터 관리

-사전은 변경 가능한 자료형이어서 실행 중에 데이터의
추가, 삭제, 수정 등의 편집을 자유롭게 할 수 있습니다.
'''
eng_kor = {"student":"학생","peach":"복숭아","book":"책"}
print(eng_kor)

'''
* 사전에 데이터 추가하기(append)
- 사전 내부에 존재하지 않는 key를 사용하여 데이터를 대입하면
데이터가 key:value 쌍으로 사전에 추가됩니다.
'''
eng_kor['grape'] = "포도"
print(eng_kor)

'''
* 사전에 데이터 수정하기
- 사전 내부에 이미 존재하는 key를 사용하여 새로운 데이터를
대입하면 해당 key값에 매핑되어있는 value값이 수정됩니다.
'''
eng_kor['book'] = '서적'
print(eng_kor)

'''
# 사전에 데이터 삭제하기(내장함수 del을 사용)
del(사전이름[key값])
'''
del(eng_kor['student'])
print(eng_kor)

'''
- 사전에 key목록과 value목록을 따로따로 추출하고 싶다면
사전의 메서드 keys(), values()를 사용합니다.

- 위 메서드들은 각각의 목록을 리스트형태로 반환합니다.
'''
print("-" * 40)
print(eng_kor.keys())
print(eng_kor.values())

# 사전에 반복문 처리
# for ~ in 뒤에 사전 데이터를 적으면 key만 반복순회합니다.
print("-" * 40)

for k in eng_kor:
    print(k,":",eng_kor[k])

# 빈 사전 만들기
d = {}
print(d)

d = dict
print(d)










