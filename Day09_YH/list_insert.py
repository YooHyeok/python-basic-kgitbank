
'''
* 리스트에 데이터를 추가하는 메서드.

1. append(): 요소를 리스트의 맨 마지막에 추가.
2. insert(): 요소를 리스트의 특정 위치에 삽입.
'''

nums = [1,3,5,7]
print(nums)

nums.append(9)
print(nums)

nums.append("안녕")
print(nums)

# nums의 2번 인덱스에 값을 저장하기 (예전에는 안됐는데 현재는 가능(3.7ver)
nums[2] = [9, 10, 11]
print(nums)

# nums의 2번 인덱스 이상 3번 인덱스 미만 영역에 들어있는
# 값을 삭제하고 요소 9, 10, 11의 값을 삽입.
nums[2:3] = [9, 10, 11]

# insert(index, value)
nums.insert(2,4) # 2번 인덱스에 4번값을 넣어라!
print(nums)

nums.insert(4, "하이")
print(nums)

# 빈 리스트를 생성하세요.
# 사용자가 그만 입력하고 싶을 때까지 음식 이름을 입력받은 후에
# 입력이 종료되면 지금까지 받았던 음식 이름을 출력하세요.

# idx = []
# fn = input("음식이름을 입력하세요:")
# idx.append(fn)
# idx.insert(idx)

foods = []
print("# 먹고 싶은 음익을 입력하세요~")
print("[그만 입력하려면  '배불러' 라고 입력하세요.]")

while True:
    food = input("> ")
    if food == "베불러":
        print("입력을 종료합니다.")
        break

    food.append(food)
print("내가 먹고 싶은 음식:" , foods)




