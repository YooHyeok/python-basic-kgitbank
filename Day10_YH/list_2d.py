
# 2차원 리스트 - 리스트 내부의 요소가 또 다시 리스트인 형태.
list_2d = [[1,2,3],[4,5,6],[7,8,9]]
print(len(list_2d))
print(type(list_2d))
print(list_2d[2])
print(type(list_2d[0]))
print(list_2d[1][2])
print(type(list_2d[0][1]))

print("-" * 40)
for li in list_2d:
    for n in li:
        print(n, end=" ")
    print()
    
# 3명의 학생의 5과목 (국,영,수,과,사) 점수 처리하기.
students = [[88, 76, 92, 98, 95],
            [65, 70, 58, 99, 100],
            [100, 95, 95, 100, 100],
            [20, 21, 10, 50, 20],
            [83, 80, 88, 100, 76]]

print("-" * 40)
stu_num = 1 # 학생들의 출석번호를 저장할 변수.
total_avgsum = 0.0 # 학생들의 평균점수의 총합을 저장할 변수.
kor_sum = 0 # 국어점수의 총점을 저장할 변수.

for student in students:
    kor_sum += student[0]
    each_sum = 0 # 1명의 5과목 총점을 저장할 변수.
    for score in student:
        each_sum += score
    each_avg = each_sum / len(student)
    total_avgsum += each_avg
    
    print("%d번 학생-> 총점: %d점, 평균: %.2f점"
          % (stu_num, each_sum, each_avg))
    stu_num += 1

total_avg = total_avgsum / len(students)
print("-" * 40)
print("우리반 평균: %.2f점" % total_avg)
print("국어 점수 평균: %.2f점" % (kor_sum / len(students)))

