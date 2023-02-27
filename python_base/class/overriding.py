# 메소드 오버라이딩 효과
'''
1. 서브클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재 정의 후 사용 가능
3. 부모클래스 메소드를 추상화 후 사용가능(구조적 접근)
4. 확장 가능, 다형성(다양한 방식으로 동작)
5. 가독성 증가

'''

# EX 1
# 기본 Overriding 예제


class ParentEx1():
    def __init__(self):
        self.value = 5
    
    def get_value(self):
        return self.value

class ChildEx1(ParentEx1) :
    pass

# 부모 클래스 메소드 호출
c1 = ChildEx1()

# c1 모든 속성 값 추출

print(f'Ex1 > {dir(c1)}')

print('')
# 부모 & 자식 모든 속성 출력 


