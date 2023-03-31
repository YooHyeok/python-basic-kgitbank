

'''
* 상속(Inheritance)

- 새로운 클래스를 설계할 때 공통 기능들을 중복해서
설계하지 않고 미리 하나의 클래스에 공통 기능들을
모아두고 데이터를 물려주는 형태.
클래스를 설계하는 객체지향 프로그래밍의 기술 중 하나입니다.

- 객체 지향 프로그래밍에서 상속이란 기존 클래스를 확장하여
새로운 클래스를 이끌어내는 것을 의미합니다.

- 상속관계는 is a 관계를 만족하는 관계입니다.
ex) 돌고래 is a 포유류 --> 돌고래는 포유류의 속성을 가지고 있다.
 
- 상속을 사용하면 클래스를 확장할 때 시간과 비용을 절감할 수 있으며
코드의 유지보수가 편리해집니다. 
'''

class Animal:
    
    def __init__(self, type, age, color, gender):
        self.type = type
        self.age = age
        self.color = color
        self.gender = gender
        
    def sound(self):
        print("낑낑깨앵")
        
    def sleep(self):
        print(self.type + "이(가) 잠을 잡니다 zzZ")
    
    def eat(self):
        print(self.type + "이(가) 밥을 먹습니다.")
        
        
# 파이썬에서 상속관계를 구현하려면
# 클래스 이름 뒤에 ()를 붙인 후 부모 클래스의 이름을 작성합니다.
class Dog(Animal):
    def __init__(self, type, age, color, gender):        
        Animal.__init__(self, type, age, color, gender)
    
    # 오버라이딩(overriding) 이란 부모클래스로부터 상속받은 특성을
    # 자식클래스에서 재정의하는 것을 의미합니다.  
    # 자식클래스의 생성자는 부모클래스의 생성자를 오버라이딩하여 작성된 것입니다.
    def sound(self):
        print("멍멍")    
        
class Human(Animal):
    def __init__(self, type, age, color, gender, job):        
        # 자식클래스에서 속성을 더하고 싶으면 더해주면 됩니다.
        Animal.__init__(self, type, age, color, gender)
        self.job = job
        
    def sound(self):
        print('안녕하세요.')
    
    def work(self): # 자식클래스의 고유 메서드(부모로부터 물려받은 것이 아님.)
        print(self.type + "의 직업은" + self.job + "입니다.")
        
baduk = Dog('강아지', 6, 'black', '수')
baduk.sound()
baduk.sleep()
baduk.eat()
print("-" * 40)

hong = Human('홍길동', 20, 'white', "남", "학생")

hong.sleep() # 부모로부터 물려받은 메서드 (자식클래스에서 선언되지 않아도 사용가능.
hong.eat()
hong.work()
hong.sound()














