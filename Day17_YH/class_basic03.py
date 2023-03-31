

'''
* 클래스

- 클래스는 객체를 만들기 위한 설계도입니다.
- 클래스는 객체의 속성(멤버변수)과 기능(메서드)의 집합입니다.
- 클래스 내부에 정의된 함수를 메서드라고 부릅니다.
'''

# 클래스 이름은 앞글자를 대문자로 지정하는 것이 관례!
class Calculator:
    
    # 클래스 안에 들여쓰기를 통해 정의된 함수를 메서드라고 부르며,
    # 메서드의 첫번째 인수는 무조건 self입니다.
    # self는 객체들을 구분하기 위한 용도의 인수값입니다.
    def setting(self, color, n1, n2): # self = 객체를 구별하기 위해서
        # self.이 붙은 변수를 객체의 속성(Attribute)
        # 또는 멤버변수 라고 부릅니다.
        self.color = color
        self.n1 = n1
        self.n2 = n2
        
    def add(self):
        return self.n1 + self.n2

'''
- 클래스가 다 정의되었다면 해당 클래스를 통해 빠르고 쉽게
객체를 생성할 수 있습니다.

- 객체 생성 문법
ex) 변수 = 클래스이름()
'''
red_calc = Calculator() # 계산기 객체가 생성됨!
blue_calc = Calculator() # 2번째 계산기 객체 생성됨!

# 객체의 속성과 기능을 사용하는 법
# 1. 객체의 속성값을 참조 -> 객체변수명.속성이름
# 2. 객체의 기능 참조 -> 객체변수명.메서드이름()

red_calc.setting("빨간색", 15, 5)
blue_calc.setting("파랑색", 20, 3)

print("빨간계산기의 색깔: ", red_calc.color)
print("파랑계산기의 색깔: ", blue_calc.color)

print("빨간 계산기의 덧셈 결과: ", red_calc.add())
print("파랑 계산기의 덧셈 결과: ", blue_calc.add())






























