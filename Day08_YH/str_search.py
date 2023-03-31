
'''
* 문자열 관리 함수, 메서드.

- 함수: 모듈 내부에서 공용적으로 사용할 수 있는 기능. (단독 호출)
- 메서드: 클래스에 소속된 함수, 특정 자료형 전용함수.(참조할 문자열을 .앞에 붙임)
'''
# 내장 함수 len(): 순차형 자료(sequence)의 내부 데이터 갯수를 구함.

s = "python programming"

count = 0
for c in s :
    count += 1
print("s의 글자 수:",count)
print("s의 글자 수:",len(s))

p = [1, 2, 3, 4, 5]
print(len(p))
print(len(range(1,1001)))

user_id = "abc123"
if len(user_id) < 6:
    print("id는 6글자 이상 작성해 주세요.")
else:
    print("id가 정상 등록되었습니다.")

'''
# 문자열 메서드 find(), rfind()
- 문자열 내부에 특정문자를 검색하여 해당 문자의
인덱스를 알려줍니다.

- find()는 앞에서부터 탐색, rfind()는 뒤에서부터 탐색.
- 탐색시 문자를 발견하지 못하면 -1을 반환.
'''
# s = "python programming"
print("=" * 40)
print(s.find("o"))
print(s.rfind("o"))

# program이 문자열변수 s에 들어있다면 해당 단어의 첫번째 글자의 인덱스를 반환.
print(s.find("program"))
print(s.find("메롱"))

pw = "fff123!4"
if pw.find("!") == -1:
    print("비밀번호에는 반드시 !를 포함시켜 주세요!")
else:
    print("비밀번호가 정상 등록되었습니다.")

# 메서드 index(): find와 효과는 동일하지만
# 단어를 탐색하지 못했을 때 에러가 발생합니다.
# print(s.index"X")

# 메서드 count(): 문자열 내부에 찾는 단어의 출현 횟수를 반환.

message = """ 생각이라는 생각은 생각하면 생각할수록 자꾸 생각이 나는\
생각이기 때문에 생각이라는 생각은 아예 생각하지 않는 생각이\
가장 좋은 생각이라고 생각한다. """

print("'생각'의 출현 횟수:",message.count("생각"))

'''
- 특정 문자가 있는 인덱스 번호 및 횟수는 관심이 없고
단순히 포함 여부만 확인하고 싶다면  in키워드를 사용합니다.

- in키워드는 문자열 내부에 찾는 단어가 포함되어 있다면
 True를, 포함되어 있지 않다면 False를 반환합니다.
'''
# s = "python programming"
print("-" * 40)
print("a" in s)
print("q" in s)
print("pro" in s)
print("z" not in s)

'''
- 사용자에게 데이터를 입력받을 때 입력값의 형태를 검사할 수 있습니다.

1. isdecimal(): 모든 문자가 숫자 형태인지를 검사.
2. isalpha(): 모든 문자가 영문 알파벳인지를 검사.
3. islower(): 모든 문자가 영문 소문자인지를 검사.
4. isupper(): 모든 문자가 영문 대문자인지를 검사.
'''

print("-" * 40)
print("15 + 8 = ??")
while True:
    print("-" * 40)
    answer = input("정답: ")
    if answer.isdecimal():
        answer = int(answer)
    else:
        print("정답은 숫자로만 입력해주세요!")
        continue
    
    if answer == 23:
        print("정답!")
        break
    else:
        print("오답!")





















