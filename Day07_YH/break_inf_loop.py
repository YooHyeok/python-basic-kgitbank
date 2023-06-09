
'''
* 무한루프

- 무한 루프 반복횟수를 정하지 않고 무한하게 반복문을 
실행하는 구조입니다.

- 처음 반복문을 구설할 때 개발자가 사전에 정확한
반복 횟수를 파악할 수 없다면 무한루프를 형성해 두고
 특정 조건을 통해 종료할 수 있도록 코드를 설계합니다.
 
- 파이썬의 무한루프는 while문으로만 작성이 가능하며
for문으로는 작성할 수 없습니다.

-일반적으로 정확한 반복 횟수를 알고 있다면  for문을 사용하고
정확한 반복 횟수를 모른다면 while을 통해 무한 루프를 형성하여
사용합니다.

ex) while True:
            반복 실행문
      if 종료조건:
        break
'''

i = 0
while True:
    if i > 15:
        break
    print(i, end=" ")
    i += 1

print("_" * 40)

print("#먹고 싶은 과일을 입력하세요.")
print("[입력을 중지 하려면 '그만' 이라고 입력하세요!]")

while True:
    fruit = input("> ")
    if fruit == "그만":
        print("입력을 중지합니다.")
        break
print("프로그램 정상 종료!")









