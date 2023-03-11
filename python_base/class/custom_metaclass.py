# Ex1
# 커스텀 메타 클래스 생성 (Type 상속 x)

# 컴포넌트식으로 클래스 내부 메소드를 다양한 클래스에 사용 가능

def cus_mul(self, d) :
    for i in range(len(self)):
        self[i] = self[i] + d

def cus_replace(self, old, new) :
    while old in self:
        self[self.index(old)] = new
        
        
# 메소드 2개 추가하여 list 상속받는 커스텀 클래스 생성
CustomList1 = type(
        'CustomList1',
        (list,), 
        {
            'desc' : '커스텀 리스트 1', 
            'cus_mul' : cus_mul,
            'cus_replace' : cus_replace,
        }
    )

# custom한 클래스로 인스턴스 생성
c1 = CustomList1([1, 2, 3, 4])

c1.cus_mul(1000)
c1.cus_replace(1001,7777)

# 커스텀 리스트 출력
print('EX 1 >', c1)

print('EX 1 >', c1.desc)
print('EX 1 >', dir(c1))
print('EX 1 >', c1[0])


# Ex2
# 커스텀 메타 클래스 생성 (Type 상속 o)

# new -> init -> call  순서

# type을 상속한 meta class
class CustomListMeta(type) :
    # 생성할 class 초기화
    # (class 이름, 상속할 클래스, namespace)
    # (self : 생성할 클래스 , object_or_name : class 이름, bases: 상속할 클래스, dict : namespace)
    def __init__(self, object_or_name, bases, dict):
        print('__init__ -> ', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)
        
    # 생성한 클래스로 인스턴스 생성 시 실행(클래스를 함수처럼 호출하도록 함)
    def __call__(self, *args, **kargs):
        # self : 생성할 클래스 , &args : 인자 
        print('__call__ -> ', self,  *args, **kargs)
        return super().__call__(*args,**kargs)

    # CustomListMeta로 class 생성 시 첫번째로 호출(메모리 할당)
    # (metacls : 메타클래스 , object_or_name : class 생성할 이름, bases: 상속할 클래스, dict : namespace)
    def __new__(metacls, name, bases, namespace):
        print('__new__ -> ', metacls, name, bases, namespace)
        # 네임스페이스 메소드 추가 및 오버라이딩
        namespace['desc'] ='커스텀 리스트2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace
        
        return type.__new__(metacls, name, bases, namespace)

# custom 메타 클래스로 클래스 생성
 
# __new__, __init__ 호출 
CustomList2 = CustomListMeta(
                'CustomList2', 
                (list, ),
                {}
                )

# 메타 클래스로 생성한 클래스로 객체 생성 시 호출
# __call__ 호출 *args : [1,2,3,4,5,6,7]
c2 = CustomList2([1,2,3,4,5,6,7])

# 상속 확인
print(CustomList2.__mro__)


        
    
    

