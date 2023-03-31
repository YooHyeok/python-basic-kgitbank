
'''
* 리스트(list)

- 리스트는 여러 개의 값을 집합적으로 저장하기 위해
사용하는 파이썬의 자료형 입니다.

- 다른 언어의 배열과 유사한 개념이며 실제로 배열과
유사한 방식으로 데이터가 관리됩니다.

- [](대괄호) 안에 요소를 콤마로 구분하여 나열합니다.

- 저장 갯수에 제한이 없어 많은 데이터를 저장할 수 있습니다.
'''
x = ['a', 'b', 10, 'd']
print(type(x))

for c in x:
    print(type(c))

print("-" * 40)

point = [88, 96, 70, 100, 90, 100]
total = 0

for p in point:
    total += p 
avg = total / len(point)
print("총점: %d점, 평균: %.2f점" % (total, avg))


























