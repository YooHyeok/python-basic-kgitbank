
'''
points.txt 파일의 숫자값을 모두 읽어서
총합과 평균을 구한 뒤
총점, 평균값을 result.txt라는 파일에
쓰는 프로그램을 작성해보세요.
'''

'''
file_path = "D:/py1230/points.txt"
try:
    f = open(file_path, "r")
    text = f.read()
    total = 0
    for t in text:
        total += t
    print("총점: ", total)
        
except:
    print("파일 로드 실패")
finally:
    f.close
'''

try:
    f = open("d:/py1230/points.txt", "r")
    # 구분자가 공백인경우.
    # numlist = f.readlines()
    numlist = f.read().split(", ")
except:
    print("파일 로드 실패!")
finally:
    f.close()

sum = 0
for num in numlist:
    score = int(num)
    sum += score
    
avg = sum / len(numlist) # 총합 / 갯수(범위)

try:
    f = open("d:/py1230/result.txt", "w")
    data = "총점: %d점, 평균: %.2f점" % (sum, avg)
    f.write(data)
    print("파일 저장이 완료되었습니다.")
except:
    print("파일 저장 실패!")
finally:
    f.close()


























