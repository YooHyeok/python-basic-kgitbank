

'''
1. User라는 클래스를 선언하시고
메서드를 선언해 주세요.

2. 메서드는 setting이라는 메서드와
User_info라는 메서드가 있습니다.

3. setting은 회원의 정보를 매개값으로 받아서
멤버변수를 선언해 주는 역할을 합니다. (name, age, gender)

4. user_info()는 회원의 정보를 단순히
출력해 주는 메서드입니다.
'''

class User:
    def setting(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
                

    def user_info(self):
        print("*** 회원 정보 ***")
        print("# 이름:", self.name)
        print("# 나이:", self.age)    
        print("# 성별:", self.gender)
        print("**************")
        
kim = User() # 변수 = 클래스명
park = User()
lee = User()

kim.setting("김철수", 32, "남성")
park.setting("박영희", 35, "여성")
lee.setting("이순신", 42, "남성")

kim.user_info()
park.user_info()
lee.user_info()

choi = User()
choi.user_info()

