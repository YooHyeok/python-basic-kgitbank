
'''
* 생성자 (constructor)

- 생성자는 객체가 생성될 때 자동으로 호출되는 메서드이며
객체가 생성되자마자 해야할 작업들을 기술하는데 사용합니다.

- 파이썬에서는 클래스 내부의 메서드 이름을 __init__로
작성하면 이 메서드를 생성자로 자동 인식합니다.

- 생성자는 객체 생성 명령에 의해 자동으로 호출됩니다.
'''

class User:
    def __init__(self, name, age, gender):
        print("생성자가 호출됨!")
        self.name = name
        self.age = age
        self.gender = gender
                

    def user_info(self):
        print("*** 회원 정보 ***")
        print("# 이름:", self.name)
        print("# 나이:", self.age)    
        print("# 성별:", self.gender)
        print("**************")
        
choi = User("최홍만", 40, "남성")
# choi.__init__(name, age, gender) # (X)
choi.user_info()


















