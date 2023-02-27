#2. class 속성과 instance 속성 

#인스턴스.__dict__
#클래스.__dict__

# 정적 메써드 - self를 받지 않음
# 따라서 인스턴스 속성에 해당 메써드가 접근할 수 없다. 
# 대신 인스턴스 메쏘드는 접근 가능 

class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

a = Calc() #인스턴스
a.add(2,3) #인스턴스에서도 호출 가능

# 클래스 메써드

'''
class 클래스이름:
    @classmethod
    def 메서드(cls, 매개변수1, 매개변수2):
        코드
        

클래스 메서드는 정적 메서드처럼 인스턴스 없이 호출할 수 있음. 
하지만 클래스 메서드는 클래스 내부에 있는 메서드에서 
클래스 속성, 클래스 메서드에 접근해야 할 때 일반적으로 사용함.

        
'''
#첫번째인자에 cls (class약자) 적기


class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때 - 인스턴스 메쏘드임
                             # 클래스 속성 count에 1을 더함
                             # 클래스속성임을 명확하게 하기위해 Person.count 로 설정
                             # 인스턴스 메서드는 클래스 속성에 접근 가능 
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    
    # cls - 인스턴스를 self로 받는 것처럼 현재 class를 받는 인자 
    # cls로 클래스 속성에 접근
    # self를 받지 않으므로 인스턴스 속성에는 접근 불가능
 
james = Person()
maria = Person()
 
Person.print_count()    # print_count()는 클래스 메써드 이므로, 인스턴스.함수명()이 아니라 클래스.함수명()
# 2명 생성되었습니다.