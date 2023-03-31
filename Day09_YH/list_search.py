
'''
 * 리스트의 탐색과 정렬
 
1. index(): 리스트에서 특정 값이 저장된 인덱스를 반환.
2. count(): 리스트 내부에 저장된 특정 요소의 갯수를 반환.
3. sort(): 리스트를 오름차 정렬.
4. reverse(): 리스트 데이터를 역순으로 정렬.
'''
points = [99, 14, 87, 100, 55, 100, 99, 100, 22]

perfect = points.count(100)
print("만점자의 수는 %d명 입니다." % perfect)

idx = points.index(87)
print("87이 저장된 위치는 %d번 입니다." % idx)

# 내장함수 len(), max(), min()
print("학생 수는 %d명 입니다." % len(points))
print("최고점수는 %d점입니다." % max(points))
print("최저점수는 %d점입니다." % min(points))

# 오름차 정렬 sort
print("-" * 40)
print(points)
points.sort()
print(points)

points.reverse()
print(points)

# 내림차 정렬 sort(reverse=True)
print("-" * 40)
nums = [144, 32, 33, 99, 22, 100, 255]
print(nums)
nums.sort(reverse = True)
 
print(nums)

# 리스트 내의 요소의 유무를 검사하려면 in키워드를사용.
food_menu = ["김밥","단무지","닭강정","김말이"]

food = input("음식명을 입력하세요: ")

if food in food_menu:
    print("주문하신 음식은 %s입니다." % food)
else:
    print(food,"(은)는 없는 메뉴입니다.")





