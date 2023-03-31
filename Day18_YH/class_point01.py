

class Student:
    
    def __init__(self):
        self.id = None
        self.name = None
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.tot = 0
        self.avg = 0.0
        self.grade = None
        
    # 학생의 정보를 입력받는 메서드.
    def input_stu_info(self):
        self.id = input("- 학번: ")
        self.name = input("- 이름: ")
        
        while True:
            try:
                self.kor = int(input("- 국어: "))
                self.eng = int(input("- 영어: "))
                self.math = int(input("- 수학: "))
                break
            except:
                print("# 점수는 숫자로만 입력하세요!")
                continue

    # 학생의 총점, 평균, 학점을 구해주는 메서드.
    def calc_tot_avg_grade(self):
        self.tot = self.kor + self.eng + self.math
        self.avg = self.tot / 3
        
        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:
            self.grade = 'B'
        elif self.avg >= 70:
            self.grade = 'C'
        elif self.avg >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    # 학생의 정보를 출력하는 메서드
    def output_stu_info(self):
        print("%4s %5s    %6d %6d %6d %8d %8.2f %8s"
              % (self.id, self.name, self.kor,
                 self.eng, self.math, self.tot,
                 self.avg, self.grade))   
        
    
# 정보 출력 UI를 제공하는 함수
def show_point_ui():
    print("\n                       *** 성적표 ***")
    print("============================================================")
    print("%5s %8s %8s %8s %8s %11s %10s %16s"
          % ("학번", "이름", "국어", "영어"
             , "수학", "총점", "평균", "학점"))     
    print("============================================================")    


if __name__ == "__main__":
    
    students = []
    
    for x in range(3):
        stu = Student()
        
        stu.input_stu_info()
        stu.calc_tot_avg_grade()
        
        students.append(stu)
    
    show_point_ui()
    for stu in students:
        stu.output_stu_info()
    