
'''
* 리스트의 요소 다루기

- 리스트는 인덱스를 통해 요소들을 관리합니다.
- 리스트를 다룰 때는 문자열과 비슷한 방식을 사용합니다.
'''
# 리스트 인덱싱
pokemon = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀']

print(type(pokemon))
print(pokemon[2])
print(type(pokemon[1]))

print(pokemon[1][2])
print(pokemon[3][:2])

# 리스트 슬라이싱 -> 리스트데이터[begin:end:step]
nums = [0,1,2,3,4,5,6,7,8,9]

print(nums[2:5:1])
print(nums[:4])
print(nums[6:])
print(nums[1:7:2])

# 리스트는 인덱싱을 통해 변수처럼 내부의 값을 변경할 수 있습니다.
print("-" * 40)
print(pokemon)

pokemon[2] = "거북왕"
print(pokemon)

pokemon[1] = "리자몽"
print(pokemon)
pokemon[4] = pokemon[0]
print(pokemon)











