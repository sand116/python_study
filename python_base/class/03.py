# 상속

# ex 1)
'''
학생 Student는 사람 Person이므로 같은 종류입니다. 
이처럼 상속은 명확하게 같은 종류이며 동등한 관계일 때 사용. 
즉, "학생은 사람이다."라고 했을 때 말이 되면 동등한 관계에 해당
그래서 상속 관계를 영어로 is-a 관계라고 부른다(Student is a Person).
파생클래스는 기반클래스를 포함하여(같은 종류임) 몇가지 특성을 더 가진다고 생각하면 쉽다.
'''

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def study(self):
        print('공부하기')
 
james = Student()   # 파생클래스 인스턴스 만들기 
james.greeting()    # 안녕하세요. -  기반 클래스 Person의 메서드 호출 가능
james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드
# 클래스 상속은 기반 클래스의 기능을 유지하면서 새로운 기능을 추가

# ex2 )
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
#print(james.hello)

# 기반 클래스의 속성을 출력하려고 하면 에러가 발생함 왜? -  기반 클래스 Person의 __init__ 메서드가 호출되지 않았기 때문
# 파생클래스를 호출한다고 해서 기반클래스의 __init__ 메써드도 같이 호출되는 것은 아님
# 해결 방법 - super()로 기반 클래스 초기화하기

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()                
        # super()는 기반 클래스를 반환 그것의 __init__()함수 실행
        #  super(Student, self).__init__()     -현재 Student 클래스의 인스턴스의 기반 클래스
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)

#   기반 클래스를 초기화하지 않아도 되는 경우
'''
- 만약 파생 클래스에서 __init__ 메서드를 생략한다면
 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 된다.
 '''


# 메서드 오버라이딩 - 파생 클래스에서 기반 클래스의 메서드를 새로 정의 오버라이딩 - 무시하다 
'''
왜 사용하는가 ?

어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 메서드 오버라이딩을 활용.
만약 Student 클래스에서 인사하는
메서드를 greeting2로 만들어야 한다면 모든 소스 코드에서 메서드 호출 부분을 greeting2로 수정해야하기때문에
이를 방지하기 위해
& 원래 기능을 유지하면서 다른 기능 추가해야할 때 사용함
'''

print('-'*100)
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting()

print('-'*100)

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        super().greeting()    # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting()

print('-'*100)

# 포함 관계 
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class PersonList:
    def __init__(self):
        self.person_list = []    # 리스트 속성에 Person 인스턴스를 넣어서 관리
 
    def append_person(self, person):    # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

p1 = Person()
p2 = Person()
p3 = Person()

pl = PersonList()
pl.append_person(p1)
pl.append_person(p2)
pl.append_person(p3)

print(pl.person_list)

'''
상속을 사용하지 않고 속성에 인스턴스를 넣어서 관리하므로 PersonList가 Person을 포함하고 있습니다.
이러면 사람 목록 PersonList와 사람 Person은 동등한 관계가 아니라 포함 관계입니다. 즉, "사람 목록은 사람을 가지고 있다."
라고 말할 수 있습니다. 그래서 포함 관계를 영어로 has-a 관계라고 부릅니다(PersonList has a Person).
'''